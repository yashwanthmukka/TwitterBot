import tweepy
import os
import twitter
consumer_key = 'LgmOAn3dLKWyzSK3vvOGLng70'
consumer_secret = 'EG8yGH9hK95A80gpLcXEjyIKzJoVex3yKjjrjitpANuUbMGWl0'
access_token = '1053102704069734400-DTkcw9g4BH5bcHb4fYpkw3jSYj9PHW'
access_secret = 'Lxhb2C7muRvMAv1nFGKVx2PorbEDIog0jNVZIOzeVygWl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet)
