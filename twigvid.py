from picamera import PiCamera
import picamera.array
import numpy as np
import subprocess
from twython import Twython
from instabot import API
import shutil
import os
from keys import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    caption_text,
    ig_user,
    ig_pass
)


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

video = open('/home/pi/Desktop/capture.mp4', 'rb')
response = twitter.upload_video(media=video, media_type='video/mp4')
twitter.update_status(status=caption_text, media_ids=[response['media_id']])
print("Video Posted to Twitter")
if os.path.exists('config'):
    shutil.rmtree('config')
thing = API()
thing.login(username=ig_user, password=ig_pass,)
thing.upload_video('/home/pi/Desktop/capture.mp4', caption=caption_text)
print("Video Posted to Instagram")
