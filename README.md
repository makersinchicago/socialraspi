# socialraspi v.001
 This repository is for the development of a travelling photobooth. It is intended to be accessible at public spaces but respective of social distancing when needed.
 
 This first version is aimed for use in makerspaces to allow their users to share their stories in a centralized stream. The camera is being built with the hq picamera and pitft plus in mind. There will also be four gpio buttons:
 
- Record Video
- Play Video
- Send Video
- Safe Shutdown

Main is the script the pi will run at boot. All other scripts are written to test functions that will be performed here. Main will wait and invite users to interact with the bot, starting with the record button.

When "record video" is pressed, the pi will record a one minute video. It will use iizukanao/picam to simultaneously record video from the picamera and audio from the alsa microphone, as well as muxing it into a mp4 file.

The video is then posted on Twitter, Instagram, and Facebook Pages.

## The scripts

**twitpic** requires api access from the twitter developers portal. It takes a locally stored image and shares it on the timeline.

**igphoto** uses standard login in credentials to do the same on the feed.

**fbtext** requires graph api access from fb's developer portal. It share a status update on a page.

**fbphoto** uses the graph api to share an image on a page. It does not allow for uploads from the local machine and relies on the url from get_twitpic

**get_twitpic** returns the url of the last image uploaded to twitter. 

These scripts above do not use the raspberry pi hardware but were useful for learning how to get things from the machine to the social networks.

## Hardware

- Raspberry Pi
  - I'm using both the Pi 4 (4GB) and PiZero W w/ header during development
- PiTFT Plus
  - I'm using the 2.8" with assembled buttons during development but will be using the 3.2" on the final build.
- Raspberry Pi HQ Camera
- 6mm C-mount lens
- Kano Computer Kit Microphone
- 10,000mAh mAh battery

## keys.py

There is one file missing that needs to be created for storing api and login information, as well as content for the posts. keys.py should be saved on the root folder and it should look like this:

    #twitter api
    consumer_key        = '__'
    consumer_secret     = '__'
    access_token        = '__'
    access_token_secret = '__'
    
    #instagram credentials
    ig_user = '__'
    ig_pass = '__'
    
    #facebook api
    fb_pg_id = '__'
    fb_access_token = '__'
    
    #content
    image = "__"
    caption_text = "__"
    twt_image = '__'

## Set up

### pitft
To use the display, we use the image and code from adafruit's [Easy Install](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install-2) page for the unit.

To ensure compatibility, we use the recommended [OSimage](https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2020-12-04/) flashed onto a sd card using the Raspberry Pi Imager.

For the raspi-config, enable the camera, ssh, and start at the command line by default.

Once the pi is set up, we initialize the display with the following

    cd ~
    sudo apt-get install -y git python3-pip
    sudo pip3 install --upgrade adafruit-python-shell click==7.0
    git clone https://github.com/adafruit/Raspberry-Pi-Installer-Scripts.git
    cd Raspberry-Pi-Installer-Scripts
    sudo python3 adafruit-pitft.py --display=28r --rotation=90 --install-type=fbcp

To make the display more legible, we run
    sudo dpkg-reconfigure console-setup
Configure it with UTF-8, Guess, VGA, and 16x28

download this repository with
    git pull https://github.com/makersinchicago/socialraspi.git
*more to come*