import requests

from keys import(
    fb_pg_id,
    fb_access_token
)

msg = 'MESSAGE TEXT'
post_url = 'https://graph.facebook.com/{}/feed'.format(fb_pg_id)

payload = {
'message': msg,
'access_token': fb_access_token
}

r = requests.post(post_url, data=payload)
print(r.text)
