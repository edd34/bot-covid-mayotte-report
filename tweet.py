import os
import tweepy
from dotenv import load_dotenv
from covid_api import res_string
load_dotenv()

api_key = os.environ.get("api_key")
api_key_secret = os.environ.get("api_key_secret")
access_token = os.environ.get("acces_token")
access_token_secret = os.environ.get("access_token_secret")

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
tweet = res_string

api.update_status(status=tweet)