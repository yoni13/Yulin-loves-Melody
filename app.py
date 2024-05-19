from flask import Flask, Response, send_from_directory, render_template, request, redirect, make_response
from markupsafe import escape
from PIL import Image, ImageDraw, ImageFont

import urllib.parse
import os
import base64
app = Flask(  # Create a flask app
    __name__
)


@app.route('/oembedapi')
def oembedapi():
  blue = escape(request.args.get('user1'))
  red = escape(request.args.get('user2'))
  json_template = {"author_name": blue + "喜歡" + red,
    "author_url": "https://"+request.host,
    "provider_name": '聽說' + blue +'喜歡' +  red ,
    "provider_url": "https://"+request.host+"/api?user1="+blue+"&user2="+red,
    "type": "photo"
    }
  return json_template



@app.route('/imageapi')
def imageapi():
  if not os.path.isdir("tmp"):
    os.mkdir("tmp")
  blue = escape(request.args.get('user1'))
  red = escape(request.args.get('user2'))

  blue_utf8 = blue.encode('utf-8')
  red_utf8 = red.encode('utf-8')
  namebase32ed = base64.b32encode(blue_utf8 + red_utf8).decode('utf-8')

  if os.path.isfile("tmp/"+namebase32ed+".png"):
    return send_from_directory("tmp", namebase32ed+".png")
  
  img = Image.open("image4api.png")
  draw = ImageDraw.Draw(img)
  # font = ImageFont.truetype(<font-file>, <font-size>)
  font = ImageFont.truetype('NotoSansTC-VariableFont_wght-instance.ttf',50)
  # draw.text((x, y),"Sample Text",(r,g,b))
  draw.text((550, 200),blue,(70,207,193),font=font)#blue
  draw.text((550, 250),"喜歡",(202,201,66),font=font)#yellow
  draw.text((550, 300),red,(274,78,78),font=font)#red

  current_path = os.getcwd()
  imgname = namebase32ed+ '.png'
  img.save(current_path+"/tmp/"+imgname)
  return send_from_directory(current_path+"/tmp/", imgname)

@app.route('/13')
def me():
  return render_template('13.html')
@app.route('/4')
def four():
  host = request.host
  return render_template('4.html',host=host)

@app.route('/api')
def api():
  host = request.host
  blue = escape(request.args.get('user1'))
  url_blue = urllib.parse.quote(blue)
  red = escape(request.args.get('user2'))
  url_red = urllib.parse.quote(red)
  return render_template('custom.html',blue=blue,red=red,host=host,url_blue=url_blue,url_red=url_red)

@app.route('/')
def index():
    return render_template('an.html')


@app.route("/favicon.ico")
def favicon():
    return redirect(
        "https://media.discordapp.net/attachments/858972718611562496/900698598612803584/A.png"
    )

