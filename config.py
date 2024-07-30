# config.py

import os

# Twitter API configuration
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY', 'your_twitter_api_key')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY', 'your_twitter_api_secret_key')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN', 'your_twitter_bearer_token')

# Reddit API configuration
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID', 'your_reddit_client_id')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET', 'your_reddit_client_secret')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT', 'your_reddit_user_agent')

# Database configuration
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///social_butterfly.db')
