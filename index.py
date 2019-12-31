from requests.auth import HTTPBasicAuth
import requests
import json
from flask import Flask, request, render_template 


app  = Flask (__name__)
@app.route('/')
def home():
    url = "https://comicvine.gamespot.com/api/issues/?api_key=6f7e42c1a04a1903ca5c2a635e441781e12a537b&format=json"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    req = requests.get(url, headers=headers)
    comics= json.loads(req.text)
    return render_template('home.html', comics=comics)


@app.route('/comicDetails/<string:api_endpoint>')
def comicDetails(api_endpoint):
    print('>>>>>>>>>>Comic Details<<<<<<<<<<<<<')
    print(api_endpoint)
    url = "https://comicvine.gamespot.com/api/issue/" + api_endpoint + "/?api_key=6f7e42c1a04a1903ca5c2a635e441781e12a537b&format=json"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    req = requests.get(url, headers=headers)
    details = json.loads(req.text)
    print(details.get('results'))
    return render_template('comicDetails.html', details = details.get('results'))

if __name__ == "__main__":
    app.run(debug=True)

    