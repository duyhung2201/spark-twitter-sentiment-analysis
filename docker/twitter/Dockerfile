FROM python:3.7

COPY . /code
EXPOSE 5000

WORKDIR /code

RUN pip install -r requirements.txt

# ENV ORDERER_IP '0.0.0.0'

ENTRYPOINT python src/twitter_app.py