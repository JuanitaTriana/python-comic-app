from requests.auth import HTTPBasicAuth
from flask import render_template
import requests
import json


def comicList():
    url = "https://comicvine.gamespot.com/api/issues/?api_key=6f7e42c1a04a1903ca5c2a635e441781e12a537b&format=json"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    auth = HTTPBasicAuth('apikey', '40f84f1bbf803bd79830d2ccca2946674c5eb847')
    req = requests.get(url, headers=headers , auth=auth)
    comics= json.loads(req.text)
    return render_template(comics=comics)

id=comicList['id']
print(id)