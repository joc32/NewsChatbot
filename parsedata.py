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
 
max_tweets = 3000

# Creation of the actual interface, using authentication
api = tweepy.API(auth)


#two queries, first does not contain filters, the second does.  
query_nofilter = 'https://twitter.com/cnnbrk/status/1006473764018835457'
query_filter = 'https://twitter.com/cnnbrk/status/1006473764018835457 -filter:videos -filter:retweets -filter:images'

#Actual API call to fetch the data. Done with tweepy cursor object.
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query_nofilter).items(max_tweets)]


#File that holds the parsed tweets
csvfile_nofilter = open('my_scraped_tweets_nofilter.csv','w')
csvwriter = csv.writer(csvfile_nofilter)

#Essential information is extracted from the previous call and stored in new list.  
outtweets = [[tweet.id_str,tweet.created_at, tweet.text.encode("utf-8")] for tweet in searched_tweets]

#count variable that holds the line / tweet count. 
count_nofilter = 0

#data is written into the csv file. 
for item in outtweets:
	csvwriter.writerow(["id","created_at","text"])
	csvwriter.writerows(outtweets)
	count_nofilter+=1

#process is repeated with different parameters. 
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query_filter).items(max_tweets)]

csvfile_filter = open('my_scraped_tweets_filter.csv','w')
csvwriter = csv.writer(csvfile_filter)

outtweets = [[tweet.id_str,tweet.created_at, tweet.text.encode("utf-8")] for tweet in searched_tweets]

count_filter = 0

for item in outtweets:
	csvwriter.writerow(["id","created_at","text"])
	csvwriter.writerows(outtweets)
	count_filter+=1

#prints out the actual line count for each query. 
print("nofilter count ", count_nofilter)	
print("filter count ", count_filter)	





