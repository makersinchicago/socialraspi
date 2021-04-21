import os

from twython import Twython
from keys import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

photo = open('IMAGE FILE.jpg', 'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status='TWEET TEXT', media_ids=[response['media_id']])
print("Image Tweeted")
