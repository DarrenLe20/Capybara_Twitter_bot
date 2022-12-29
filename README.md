# Daily Capybara Bot

A Twitter bot that tweets a gif of a capybara every 24 hours.

## How it works

The bot is written in Python and uses the [Tweepy](https://www.tweepy.org/) library to interact with the Twitter API. The bot exracts a random GIF with the hashtag "
capybaras" from [Giphy](https://giphy.com/) and tweets it every 24 hours.

## Running the bot locally

1. Clone the repository
2. Create a virtual environment and install the dependencies fromn the requirements.txt file

      ```pip install -r requirements.txt```

3. Create a Twitter developer account and create a new app [here](https://developer.twitter.com/)
4. Generate the necessery keys and tokens for the app
5. Create a Giphy developer account and create a new app [here](https://developers.giphy.com/)
6. Generate the GIPHY SDK key for the app
7. Create a config.py file in the root directory of the project and declare the following variables

      ```API_KEY = "your_api_key"```

      ```API_SECRET_KEY = "your_api_secret_key"```

      ```ACCESS_TOKEN = "your_access_token```

      ```ACCESS_TOKEN_SECRET = "your_access_secret_token```

      ```GIPHY_API_KEY = "your_giphy_key"```

## Author

[Darren Le](https://github.com/DarrenLe20)
