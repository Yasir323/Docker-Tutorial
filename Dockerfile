FROM continuumio/anaconda:4.4.0

COPY ./flask_demo /usr/local/python/

EXPOSE 5000

WORKDIR /usr/local/python/

RUN pip install -r requirements.txt \
CMD python pred_model.py
