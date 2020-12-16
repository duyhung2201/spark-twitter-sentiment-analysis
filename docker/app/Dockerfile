FROM python:3.7
 
COPY . /code
EXPOSE 9090

WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT python src/app.py