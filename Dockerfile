FROM python:3.11
EXPOSE 1234
WORKDIR /opt/app
RUN \
    if [ `dpkg --print-architecture` = "armhf" ]; then \
    printf "[global]\nextra-index-url=https://www.piwheels.org/simple\n" > /etc/pip.conf ; \
    fi
COPY . /opt/app

RUN chmod +x rmtmp.sh

RUN touch /etc/cron.d/hello-cron/crontab

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron


RUN apt-get update
RUN apt-get -y install cron

# Add the cron job
RUN crontab -l | { cat; echo "0 * * * * bash /opt/app/rmtmp.sh"; } | crontab -


RUN pip install -r requirements.txt --no-cache-dir --upgrade
CMD ["gunicorn", "--bind", "0.0.0.0:1234", "app:app", "--log-level", "debug" ,"--error-logfile" ,"gunicorn_error.log"]

