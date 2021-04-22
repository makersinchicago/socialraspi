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
import subprocess

from keys import (
    image,
)

snapButton = Button(27)
vidButton = Button(23)
exitButton = Button(17)

with picamera.PiCamera() as camera:
        camera.resolution = (3280, 2464)
        camera.rotation = 0
        camera.start_preview()
        while True:
            if snapButton.is_pressed:
                print("Pic Mode")
                camera.capture(image)
                camera.stop_preview()
                import twitpic
                import igphoto
                camera.start_preview()
            elif vidButton.is_pressed:
                print("vid Mode")
                camera.stop_preview()
                camera.resolution = (1080, 810)
                camera.rotation = 0
                camera.start_preview()
                camera.start_recording('/home/pi/Desktop/capture.h264', format='h264')
                camera.wait_recording(5)
                camera.stop_recording()
                camera.stop_preview()
                cp = subprocess.run(["rm /home/pi/Desktop/capture.mp4"],shell=True)
                cp = subprocess.run(["MP4Box -add /home/pi/Desktop/capture.h264 /home/pi/Desktop/capture.mp4"],shell=True)
                import twigvid
            elif exitButton.is_pressed:
                exit()
            else:
                print(" ")
            sleep(.1)