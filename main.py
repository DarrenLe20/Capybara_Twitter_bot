import requests
import tweepy as tp
import urllib.parse as parse

import config


# Authenticate to Twitter
def api_auth():
    auth = tp.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    api = tp.API(auth)
    return api


def get_gif():
    url = "http://api.giphy.com/v1/gifs/search"
    params = parse.urlencode({
        "q": "capybara",
        "api_key": config.GIPHY_API_KEY,
        "limit": "1"
    })


def tweet(api, text):
    api.update_status(text)
    print("Tweeted successfully!")


if __name__ == "__main__":
    api = api_auth()
    tweet(api, "Hello, world!")
