##this script take a picture and shares it to twitter and instagram
import os
from picamera import PiCamera
from time import sleep
import picamera.array
import subprocess

from instabot import Bot
import shutil

from twython import Twython
from keys import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    ig_user,
    ig_pass,
    image,
    caption_text
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

with picamera.PiCamera() as camera:
        camera.resolution = (3280, 2464)
        camera.rotation = 0
        camera.start_preview()
        sleep(2)
        camera.capture(image)
        camera.stop_preview()

import twitpic
import igphoto
