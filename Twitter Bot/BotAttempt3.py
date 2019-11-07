# themodelbot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = 'LgmOAn3dLKWyzSK3vvOGLng70'
consumer_secret = 'EG8yGH9hK95A80gpLcXEjyIKzJoVex3yKjjrjitpANuUbMGWl0'
access_token = '1053102704069734400-DTkcw9g4BH5bcHb4fYpkw3jSYj9PHW'
access_secret = 'Lxhb2C7muRvMAv1nFGKVx2PorbEDIog0jNVZIOzeVygWl'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('models')

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    
    time.sleep(10)

