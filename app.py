import random, sys, time
from flask import Flask, Response, send_from_directory, render_template, request, redirect, make_response
import random
from markupsafe import escape


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of  for static files
)


@app.route('/12')
def twelve():
  return render_template('12.html')
@app.route('/13')
def me():
  return render_template('13.html')
@app.route('/4')
def four():
  return render_template('4.html')

@app.route('/api')
def api():
  blue = escape(request.args.get('user1'))
  red = escape(request.args.get('user2'))
  return render_template('7.html',blue=blue,red=red)

@app.route("/set")
def setcookie():
    resp = redirect('/403')
    resp.set_cookie(key='ban', value='just ban', expires=time.time() + 172800)
    f = open("403.txt", "a")
    f.write(request.headers.get('user-agent'))
    f.write("\n")
    f.close
    return resp


@app.route('/403')
def denied():
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(500)
def Server_Error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('an.html')


@app.route("/favicon.ico")
def favicon():
    return redirect(
        "https://media.discordapp.net/attachments/858972718611562496/900698598612803584/A.png"
    )

