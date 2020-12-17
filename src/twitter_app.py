import socket
import sys
import requests
import requests_oauthlib
import json

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Replace the values below with yours
ACCESS_TOKEN = '2455225267-2OeMn8aeXvLXgW5f4Y8SmfBA305Jsbocxs2colW'
ACCESS_SECRET = 'qShVTPlCY4MYpTaBQWsNGwP4LKvdDqOEuuF190499BrlZ'
CONSUMER_KEY = '3WaQCIqrBhjoSUah4lTjxxkhV'
CONSUMER_SECRET = 'ONnaKHhZwhZmOlNFCEjDzEHi03Za3V9UwwjPPZzjFOGTYl2uK9'
my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)

print("Starting twitter app...", flush=True)

analyzer = SentimentIntensityAnalyzer()

def process_send_tweets_to_spark(http_resp, tcp_connection):
    for line in http_resp.iter_lines():
        try:
            full_tweet = json.loads(line)
            tweet_text = str(full_tweet['text'].encode("utf-8"))
            
            # analysis sentiment score
            sentiment_score = analyzer.polarity_scores(tweet_text)["compound"]
            if sentiment_score >= 0.05:
                sentiment = "POSITIVE"
            elif sentiment_score <= -0.05:
                sentiment = "NEGATIVE"
            else:
                sentiment = "NEUTRAL"

            # separate sentiment label with tweet content
            mess =  sentiment + '||||' + tweet_text + '\n' 

            tcp_connection.send(bytes(mess, 'utf-8'))
        except:
            e = sys.exc_info()[0]
            print("Error: %s" % e, flush=True)


def get_tweets():
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    # get tweet from @realDonaldTrump 25073877
    # @twitter 783214
    # @cnn 759251
    # @ellen 15846407
    # @BarackObama 813286
    # @cnnbrk 428333
    # @BBCWorld 742143
    # @BBCBreaking 5402612
    # @joebiden 939091
    # @FoxNews 1367531
    # @elonmusk 44196397
    # @billgates 50393960 
    # @nytimes 807095
    # @washingtonpost 2467791
    # @ellen 15846407
    query_data = [('language', 'en'), ('follow', '25073877'), ('follow', '783214'), ('follow', '759251'), \
        ('follow', '15846407'), ('follow', '813286'), ('follow', '428333'), ('follow', '742143'), \
        ('follow', '5402612'), ('follow', '939091'), ('follow', '1367531'), ('follow', '44196397'), \
        ('follow', '50393960'), ('follow', '807095'), ('follow', '2467791'), ('follow', '15846407')]
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    response = requests.get(query_url, auth=my_auth, stream=True)
    print(query_url, response, flush=True)

    return response

TCP_IP = "0.0.0.0"
TCP_PORT = 5001
conn = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Waiting for TCP connection...", flush=True)
conn, addr = s.accept()
print("Connected... Starting getting tweets.", flush=True)
resp = get_tweets()
process_send_tweets_to_spark(resp, conn)



