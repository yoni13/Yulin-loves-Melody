FROM python:3.11
EXPOSE 1234
WORKDIR /opt/app
RUN \
    if [ `dpkg --print-architecture` = "armhf" ]; then \
    printf "[global]\nextra-index-url=https://www.piwheels.org/simple\n" > /etc/pip.conf ; \
    fi
COPY . /opt/app
RUN pip install -r requirements.txt --no-cache-dir --upgrade
CMD ["gunicorn", "--bind", "0.0.0.0:1234", "app:app"]

