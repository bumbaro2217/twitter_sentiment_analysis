import tweepy
from textblob import TextBlob
import csv

consumer_key = 'uix5KfiR7aar0s5n8BHFhIkFr'
consumer_secret = 'UAPA5eFX0FzbMoZe05XYuFrKfHVdpNLzE2GbSDAVrnr0zt12nh'

access_token = '38360777-WtNAtMyZzVDbfj6MEibbc2XvcV5oTky3iwMWoKYlF'
access_token_secret = 'DONLOJZd2DdUmqzsogN5rHImjD1PMqFnlgclHRgboKysA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

public_tweets = api.search('trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    


# Write a row to the CSV file.
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), analysis.sentiment])
    if analysis.sentiment.polarity >= 0:
        csvWriter.writerow(['Positive'])
    else: csvWriter.writerow(['Negative'])
    print tweet.created_at, tweet.text
csvFile.close()
