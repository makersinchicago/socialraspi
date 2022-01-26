"""

at boot, present prompt

wait for user input

at user input, record 1 minute of video and audio using picam

after recording is done, present prompt. user may play back video or record anew

if the user is satisfied, they may press send to post the video to makersinchicago's twitter timeline, the chimakerfest's ig feed, and the chimakerfest facebook page.

the is notified that the posts have been uploaded and the prompt is presented for the next user.

there is a fourth button to enable a safe shutdown, it is located near the power switch.

"""

import alsaaudio, wave, numpy
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

tracktime = 2832

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
#                import igphoto
                camera.start_preview()
            elif vidButton.is_pressed:
                print("vid Mode")
                camera.stop_preview()
                camera.resolution = (1080, 810)
                camera.rotation = 0
                camera.start_preview()
                inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
                inp.setchannels(1)
                inp.setrate(48000)
                inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
                inp.setperiodsize(1024)
                camera.start_recording('/home/pi/Desktop/capture.h264', format='h264')
                w = wave.open('/home/pi/Desktop/audio.wav', 'w')
                w.setnchannels(1)
                w.setsampwidth(2)
                w.setframerate(48000)
                while tracktime > 0:
                    tracktime -= 1
                    l, data = inp.read()
                    a = numpy.fromstring(data, dtype='int16')
                    print(numpy.abs(a).mean())
                    w.writeframes(data)
                camera.stop_recording()
                camera.stop_preview()
                cp = subprocess.run(["ffmpeg -y -i /home/pi/Desktop/audio.wav -codec:a aac /home/pi/Desktop/audio.aac"],shell=True)
                cp = subprocess.run(["rm /home/pi/Desktop/capture.mp4"],shell=True)
                cp = subprocess.run(["MP4Box -add /home/pi/Desktop/capture.h264:fps=30 -add /home/pi/Desktop/audio.aac /home/pi/Desktop/capture.mp4"],shell=True)
                cp = subprocess.run(["rm /home/pi/Desktop/capture.h264"],shell=True)
                cp = subprocess.run(["rm /home/pi/Desktop/audio.wav"],shell=True)
                cp = subprocess.run(["rm /home/pi/Desktop/audio.mp3"],shell=True)
                import twigvid
                camera.resolution = (3280, 2464)
                camera.rotation = 0
                camera.start_preview()
            elif exitButton.is_pressed:
                exit()
            else:
                print("x")
            sleep(.1)
