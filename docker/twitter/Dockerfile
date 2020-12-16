FROM python:3.7

COPY . /code
EXPOSE 5001

WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT python src/twitter_app.py