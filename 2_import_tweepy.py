import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'rm3PZ9TzVoZxBwoKRNKTnZx6V'
consumer_secret= 'EhhzwZouxE4O5XwHLvGD25vr1aqw9X1lhpnjKNBLdtQEDZOW2F'

access_token='384518822-V5Bh19jOyCHYS5cc5kis7MWX5yjvSkc2XRrIDHNL'
access_token_secret='9QeJGwXsT8upHBfR5RdDTG0xOSlGFxMZlUQgUXlnyNAs4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Bolsonaro')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")