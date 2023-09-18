from flask import Flask, render_template
import requests
import json
from threading import local

tls = local()
app = Flask(__name__)

def getMeme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = getMeme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)
