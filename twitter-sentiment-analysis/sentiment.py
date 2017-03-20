import sys
import tweepy
from textblob import TextBlob

tweet_count_max = 100

# Dicts hold tweet (key) and polarity (value)
negative_dict = {}
positve_dict = {}
neutral_dict = {}

def categorize_tweet(tweet):
    text = tweet.text
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    text = text.encode("utf-8")

    if polarity > 0:
        positve_dict[text] = polarity
        return 'positive'
    elif polarity == 0:
        neutral_dict[text] = polarity
        return 'neutral'
    else:
        negative_dict[text] = polarity
        return 'negative'

def save_to_file(word):
    f = open('%s.csv' % word, 'w')
    f.write("Positive Tweets: \n")
    f.write("----------------\n")
    for tweet in positve_dict:
        f.write(tweet + "\n")

    f.write("\nNegative Tweets: \n")
    f.write("----------------\n")
    for tweet in negative_dict:
        f.write(tweet + "\n")

    f.write("\nNeutral Tweets: \n")
    f.write("---------------\n")
    for tweet in neutral_dict:
        f.write(tweet + "\n")

# Authenticate
try:
    consumer_key = 'O06yYbcTmE2Ib2aHKxlGtdB1T'
    consumer_secret = 'Rdl9yEGIXmmeZV5EwxGCJz79ZGDIsP0cEagoRWt9NIM6clwZEL'

    access_token = '1902268832-Q4jygOo1jZ9lZqJSSWkHhcQUo9ihYvIkV1jIQor'
    access_token_secret = 'L4slTwSXx7evialWAlF4N6useMeLqR2csukhhOc8pJy3a'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
except:
    print("Authentication Error!")
    sys.exit(1)

# Get word to search for through command arg
try:
    word = sys.argv[1]
    public_tweets = api.search(q=word, count=tweet_count_max)
except:
    print("Error! -- Usage: sentiment.py <WORD TO SEARCH>")
    sys.exit(1)

# Go through each tweet and place in either negative, neutral, or positve dicts
for tweet in public_tweets:
    categorize_tweet(tweet)

# Save tweets to CSV file
save_to_file(word)

# Print out sentiment results
title = "\nResults for \"" + word + "\" in last " + str(tweet_count_max) + " tweets:"
print(title)
print("-" * len(title))
print("Positve = " + str(len(positve_dict)))
print("Negative = " + str(len(negative_dict)))
print("Neutral = " + str(len(neutral_dict)) + "\n")
