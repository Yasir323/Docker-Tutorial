FROM continuumio/anaconda3:latest
EXPOSE 8000
RUN  apt-get update && apt-get install -y apache2 \
    apache2-dev \
    vim \
 && apt-get clean \
 apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/pred_model/
COPY ./pred_model.wsgi /var/www/pred_model/pred_model.wsgi
COPY ./flask_demo /var/www/pred_model/
RUN pip install -r requirements.txt
RUN /opt/conda/bin/mod_wsgi-express install-module
RUN mod_wsgi-express setup-server pred_model.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND
