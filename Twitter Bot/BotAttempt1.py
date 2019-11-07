import tweepy
import  sys
import time
import requests


def tweetToTwitter():
    consumer_key = 'LgmOAn3dLKWyzSK3vvOGLng70'
    consumer_secret = 'EG8yGH9hK95A80gpLcXEjyIKzJoVex3yKjjrjitpANuUbMGWl0'
    access_token = '1053102704069734400-DTkcw9g4BH5bcHb4fYpkw3jSYj9PHW'
    access_secret = 'Lxhb2C7muRvMAv1nFGKVx2PorbEDIog0jNVZIOzeVygWl'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    responeData = requests.get("http://api.icndb.com/jokes/random/?escape=javascript")
    mystatustext = str(responeData.json()['value']['joke'])
    api.update_status(status=mystatustext)


def main():
    print('#HappyBirthdayPrabhas')
while True:
        try:
            tweetToTwitter()
            time.sleep(60)  # 1 minute
            
        except :
            pass
    
        

if __name__ == "__main__":
    main()
