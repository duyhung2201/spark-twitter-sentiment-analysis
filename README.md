# Sentiment Analysis with PySpark

# How it looks

![alt tag](https://github.com/duyhung2201/spark-twitter-sentiment-analysis/blob/ngocbh/docs/demo.png?raw=true)

# How to run
Run by docker

```
docker-compose up
```

Or run by ```python```
```
python src\twitter_app.py
spark-submit --master "local[*]" src\spark_app.py
python src\app.py
```

Access ```https://0.0.0.0:9090``` vs Unix user or ```https://127.0.0.1:9090``` vs Window user
