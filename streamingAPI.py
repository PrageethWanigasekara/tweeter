import tweepy
import socket
import requests
import time
from tweepy import OAuthHandler
import csv
#from authentication import authentication  # Consumer and access token/key

csvFile = open('tweetresult.csv', 'a')
csvWriter = csv.writer(csvFile)

class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        get_tweet(status)
        get_user_informations(status)
        #csvWriter.writerow([status.author.screen_name,status.created_at, status.text.encode('utf-8')])
        print '\n'

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False


def get_tweet(tweet):
    print("Tweet Message : " + tweet.text)
    #print("Tweet Favorited \t:" + str(tweet.favorited))
    #print("Tweet Favorited count \t:" + str(tweet.favorite_count))

    # Display sender and mentions user



def get_user_informations(tweet):
    print("User ID \t:" + str(tweet.user.id))
    print("User image profil \t:" + tweet.user.profile_image_url_https)
    print("User Name \t:" + tweet.user.name)
    print("User URL \t:", tweet.user.url)
    print("User profil text color \t:" + tweet.user.profile_text_color)
    print("User background image url \t:" + tweet.user.profile_background_image_url)
    print("User Friends count \t:" + str(tweet.user.friends_count))
    print("User Screen name \t:" + tweet.user.screen_name)
    print("User Verified \t:" + str(tweet.user.verified))
    print("User Favorite count \t:" + str(tweet.user.favourites_count))

    if hasattr(tweet.user, 'time_zone'):
        print("User Time zone \t:", tweet.user.time_zone)
        print("User UTC Offset \t:" + str(tweet.user.utc_offset))
        print("User Status count \t:" + str(tweet.user.statuses_count))

        print("User Description \t:", tweet.user.description)
        print("User Follower count \t:" + str(tweet.user.followers_count))
        print("User Created at \t:" + str(tweet.user.created_at))


if __name__ == '__main__':

    # Get access and key from another class


    consumer_key='VGqIqCx4SzyF3MekfmjOydNdp'
    consumer_secret='xevr5Auxcs0kAEBB0k8GBLPX97quIgtiKDuLv39hTNhwm3KHkC'
    access_token_key='841302681708765184-mb3KdzpclXXneJGDi9w60zTe3PaiWDH'
    access_token_secret='1jWTRLHiZ55nKgiiAgMLewicnNlpzQqVv6sOm0VlhGxkD'

    # Authentication
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)

    streamListener = TwitterStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)
    print '1'
    myStream.filter(track=['michael'], async=True)
    print '2'

