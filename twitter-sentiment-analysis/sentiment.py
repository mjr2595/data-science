import sys
import tweepy
from textblob import TextBlob

# Authenticate
consumer_key = 'O06yYbcTmE2Ib2aHKxlGtdB1T'
consumer_secret = 'Rdl9yEGIXmmeZV5EwxGCJz79ZGDIsP0cEagoRWt9NIM6clwZEL'

access_token = '1902268832-Q4jygOo1jZ9lZqJSSWkHhcQUo9ihYvIkV1jIQor'
access_token_secret = 'L4slTwSXx7evialWAlF4N6useMeLqR2csukhhOc8pJy3a'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Get word to search for through command arg
word = sys.argv[1]
try:
    public_tweets = api.search(word)
except:
    print("Error! -- Usage: sentiment.py <WORD TO SEARCH>")

# Dicts hold tweet (key) and polarity (value)
negative_dict = {}
positve_dict = {}
neutral_dict = {}

# Go through each tweet and place in either negative, neutral, or positve dicts
for tweet in public_tweets:
    categorize_tweet(tweet)

# Save tweets to CSV file
save_to_file(word)

# Print out sentiments in order of popularity


# Helper functions
def categorize_tweet(tweet):
    text = tweet.text
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        positve_dict[text] = polarity
        return 'positive'
    elif polarity == 0:
        neutral_dict[text] = polarity
        return 'neutral'
    else:
        negative_dict[text] = polarity
        return 'negative'
