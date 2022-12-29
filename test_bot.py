import unittest
import main
import requests


class TestBot(unittest.TestCase):
    def test_bot(self):
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
        date = main.get_current_date()
        self.assertTrue(date)

    def test_twitter_auth(self):
        api = main.api_auth()
        self.assertTrue(api)
