import tweepy

from keys import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

timeline = tweepy.Cursor(api.user_timeline, tweet_mode='extended').items() 
tweet = next(timeline)

print(tweet.entities['media'][0]['media_url'])
