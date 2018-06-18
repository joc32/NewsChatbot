import tweepy
import time
import csv
import API_keys

# Consumer keys and access tokens, used for OAuth
ck = API_keys.consumer_key
cs = API_keys.consumer_secret
at = API_keys.access_token
ats = API_keys.access_token_secret


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(at, ats)
 
# Creation of the actual interface, using authentication
# The script waits in case the API is overloaded with requests. 
api = tweepy.API(auth, wait_on_rate_limit=True)
 
query = 'https://twitter.com/cnnbrk/status/1006473764018835457 -filter:retweets'
max_tweets = 500


#Actual API call to fetch the data. Done with tweepy cursor object.
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

#File that holds the parsed tweets
csvfile = open('my_scraped_tweets.csv','w')
csvwriter = csv.writer(csvfile)

#Essential information is extracted from the previous call and stored in new list.  
outtweets = [[tweet.id_str,tweet.created_at, tweet.text.encode("utf-8")] for tweet in searched_tweets]

#data is written into the csv file. 
for item in outtweets:
	csvwriter.writerow(["id","created_at","text"])
	csvwriter.writerows(outtweets)






