# Daily Capybara Bot

A Twitter bot that tweets a gif of a capybara every 24 hours.

Twitter: [@capyenjoyerbot](https://twitter.com/capyenjoyerbot)

## How it works

The bot is written in Python and uses the [Tweepy](https://www.tweepy.org/) library to interact with the Twitter API. The bot extracts a random GIF with the hashtag "
capybaras" from [Giphy](https://giphy.com/) and tweets it every 24 hours.

## Running the bot locally

1. Clone the repository
2. Create a virtual environment and install the dependencies fromn the requirements.txt file

      ```pip install -r requirements.txt```

3. Create a Twitter developer account and create a new app [here](https://developer.twitter.com/)
4. Generate the necessery keys and tokens for the app
5. Apply for elevated access to the Twitter API
6. Create a Giphy developer account and create a new app [here](https://developers.giphy.com/)
7. Generate the GIPHY SDK key for the app
8. Createa .env file with the following environment variables

      ```API_KEY="your_api_key"```

      ```API_SECRET_KEY="your_api_secret_key"```

      ```ACCESS="your_access_token"```

      ```ACCESS_SECRET="your_access_secret_token"```

      ```GIPHY_KEY="your_giphy_key"```

9. Create a config.py file in the root directory of the project and declare the following variables

      ```SLEEP_TIME = 86400```

## Docker

## Author

[Darren Le](https://github.com/DarrenLe20)
