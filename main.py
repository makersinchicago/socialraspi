"""

at boot, present prompt

wait for user input

at user input, record 1 minute of video and audio using picam

after recording is done, present prompt. user may play back video or record anew

if the user is satisfied, they may press send to post the video to makersinchicago's twitter timeline, the chimakerfest's ig feed, and the chimakerfest facebook page.

the is notified that the posts have been uploaded and the prompt is presented for the next user.

there is a fourth button to enable a safe shutdown, it is located near the power switch.

"""

import os
from picamera import PiCamera
from time import sleep
import picamera.array
from gpiozero import Button

from keys import (
    image,
)

snapButton = Button(27)
exitButton = Button(17)

with picamera.PiCamera() as camera:
        camera.resolution = (3280, 2464)
        camera.rotation = 0
        camera.start_preview()
        while True:
            if snapButton.is_pressed:
                print("Pressed")
                camera.capture(image)
                camera.stop_preview()
                import twitpic
                import igphoto
                camera.start_preview()
            elif exitButton.is_pressed:
                exit()
            else:
                print("Released")
            sleep(.1)