import os

from twython import Twython
from keys import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    image,
    caption_text
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

photo = open(image, 'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=caption_text, media_ids=[response['media_id']])
print("Tweeter Success")
