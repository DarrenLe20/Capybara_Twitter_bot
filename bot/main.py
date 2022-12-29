#!/usr/bin/env python3

from urllib import parse, request
import requests
import json
import os
import tweepy as tp
from time import sleep
from datetime import date

# import ./config.py where keys are stored
import config


# Authenticate to Twitter
def api_auth():
    auth = tp.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET_KEY"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"),
                          os.getenv("ACCESS_SECRET_TOKEN"))
    api = tp.API(auth)
    return api


def get_gif():
    url = "http://api.giphy.com/v1/gifs/random"
    params = parse.urlencode({
        "tag": "capybaras",
        "api_key": os.getenv("GIPHY_API_KEY"),
    })
    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
    return data


def get_current_date():
    today = date.today().strftime("%B %d, %Y")
    return today


def tweet(api):
    gif_data = get_gif()
    gif = gif_data["data"]["images"]["downsized"]["url"]
    data = requests.get(gif).content
    # download gif
    with open("image.gif", "wb") as f:
        f.write(data)
        f.close()
    # tweet gif with date
    msg = get_current_date()
    api.update_with_media("image.gif", msg)


if __name__ == "__main__":
    api = api_auth()
    while True:
        tweet(api)
        sleep(config.SLEEP_TIME)
        # break
