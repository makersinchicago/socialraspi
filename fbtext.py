import requests

from keys import(
    fb_pg_id,
    fb_access_token,
    twt_image
)

#init
caption = 'CAPTION TEXT'
target_url = 'https://graph.facebook.com/{}/photos'.format(fb_pg_id)
image_location = twt_image

#prep
payload = {
'url': image_location,
'caption': caption,
'access_token': fb_access_token
}

#executes $POST
r = requests.post(target_url, data=payload)
print(r.text)
