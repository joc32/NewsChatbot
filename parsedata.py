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

max_tweets=500 

#list of 10 articles that are grabbed from Twitter. With specific filters. 
query = 'https://twitter.com/cnnbrk/status/1009478800416083968 -filter:videos -filter:retweets -filter:images'
query1 = 'https://twitter.com/cnnbrk/status/1009518811618402306 -filter:videos -filter:retweets -filter:images'
query2 = 'https://twitter.com/cnnbrk/status/1010231521784025091 -filter:videos -filter:retweets -filter:images'
query3 = 'https://twitter.com/cnnbrk/status/1010878074051809280 -filter:videos -filter:retweets -filter:images'
query4 = 'https://twitter.com/cnnbrk/status/1011749396155858944 -filter:videos -filter:retweets -filter:images'

query5 = 'https://twitter.com/FoxNews/status/1011838534561378304 -filter:videos -filter:retweets -filter:images'
query6 = 'https://twitter.com/FoxNews/status/1011950342962020357 -filter:videos -filter:retweets -filter:images'
query7 = 'https://twitter.com/FoxNews/status/1012055217377030144 -filter:videos -filter:retweets -filter:images'
query8 = 'https://twitter.com/FoxNews/status/1012060514569129984 -filter:videos -filter:retweets -filter:images'
query9 = 'https://twitter.com/FoxNews/status/1012073583709913094 -filter:videos -filter:retweets -filter:images'


#Initialisation of appropriate lists. One for Files one for Queries. 
file_list = ['article.csv','article1.csv','article2.csv','article3.csv','article4.csv','article5.csv','article6.csv','article7.csv','article8.csv','article9.csv']
query_list = [query,query1,query2,query3,query4,query5,query6,query7,query8,query9]


#Loop that calls the API call, opens a file, puts the file into a csv writer, and writes the appropriate data. 
for index in range(0,10):
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query_list[index],lang='en',tweet_mode='extended').items(max_tweets)]
	file = open(file_list[index],'w')
	csvwriter = csv.writer(file)
	outtweets = [[tweet.full_text] for tweet in searched_tweets]
	for item in outtweets:
		csvwriter.writerows(outtweets)
	index+=1




