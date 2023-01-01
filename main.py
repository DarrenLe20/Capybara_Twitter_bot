#!/usr/bin/env python3

from urllib import parse, request
from dotenv import load_dotenv
import requests
import json
import os
import tweepy as tp
from datetime import date

load_dotenv()


# Authenticate to Twitter
def api_auth():
    auth = tp.OAuth1UserHandler(
        os.getenv("API_KEY"), os.getenv("API_SECRET_KEY"))
    auth.set_access_token(os.getenv("ACCESS"), os.getenv("ACCESS_SECRET"))
    api = tp.API(auth)
    return api


def get_gif(tag="capybaras"):
    url = "http://api.giphy.com/v1/gifs/random"
    params = parse.urlencode({
        "tag": tag,
        "api_key": os.getenv("GIPHY_KEY"),
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
    api.update_status_with_media(msg, "image.gif")


def get_msg(api):
    msgs = api.list_direct_messages()  # 20 msgs default
    for message in reversed(msgs):
        sender = message.message_create["sender_id"]
        content = message.message_create["message_data"]["text"]
        api.destroy_direct_message(message.id)


if __name__ == "__main__":
    api = api_auth()
    tweet(api)
