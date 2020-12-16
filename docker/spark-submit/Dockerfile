FROM bde2020/spark-base:3.0.1-hadoop3.2

COPY . /code

WORKDIR /code

RUN python3 -m pip install -r requirements.txt

ENV SPARK_MASTER_NAME spark-master
ENV SPARK_MASTER_PORT 7077
ENV SPARK_APPLICATION_PYTHON_LOCATION ./src/spark_app.py
ENV SPARK_APPLICATION_ARGS ""
ENV ENABLE_INIT_DAEMON false

COPY ./docker/spark-submit/submit.sh /

ENTRYPOINT ["/bin/bash", "/submit.sh"]