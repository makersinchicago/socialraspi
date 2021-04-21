import subprocess
import shutil
import os

from instabot import Bot
from keys import(
    ig_user,
    ig_pass,
    image,
    caption_text
)

if os.path.exists('config'):
        shutil.rmtree('config')

bot = Bot()

bot.login(username=ig_user, password=ig_pass,)
bot.upload_photo(image, caption=caption_text)
print("Image Posted to Instagram")
