import unittest
import main
import requests
from datetime import date


class TestBot(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_GIF_retrieval(self):
        data = main.get_gif()
        self.assertTrue(data["data"]["images"]["downsized"]["url"])

    def test_GIF_download(self):
        data = main.get_gif()
        gif = data["data"]["images"]["downsized"]["url"]
        data = requests.get(gif).content
        # test if image.gif exists
        with open("image.gif", "wb") as f:
            f.write(data)
            f.close()
        self.assertTrue("image.gif")

    def test_date_retrieval(self):
        res = main.get_current_date()
        expected = date.today().strftime("%B %d, %Y")
        self.assertTrue(res == expected)

    def test_twitter_auth(self):
        api = main.api_auth()
        self.assertTrue(api)

    def test_get_followers(self):
        api = main.api_auth()
        followers = api.get_follower_ids()
        self.assertTrue(followers)

    def test_media_upload(self):
        api = main.api_auth()
        media = api.media_upload(filename="image.gif")
        self.assertTrue(media)
