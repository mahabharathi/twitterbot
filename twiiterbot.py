import tweepy
import time
import sys

auth = tweepy.OAuthHandler('FzQNofWMcCfK1ghaqpwM3sCJu', 'fLOq2aNCMaZs7Uk49m0DonIYuwriSSaXlrdyxPjZGiQ6CpOKlq')
auth.set_access_token('982510959246782465-rF403MTsO6jwX15k5NEt4cepsB8yCv5', 'bkjjJlr0dMOv3gPGZWYErSZ5dFX0z4kDxJnwZtE8Meoqo')

api = tweepy.API(auth)
'''user=api.me()
print(user.name,user.screen_name,user.followers_count)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
'''
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        print("Limit Handle Exceeded. Sleeping for 7 minutes.")
        time.sleep(10) 
    except StopIteration:
        return
    
#Generous bot
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name,follower.followers_count)

#seach keywords python
numberOfTweets=2
search_str='indiaforsale'

for tweet in tweepy.Cursor(api.search,search_str).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break