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
query = 'https://twitter.com/CNN/status/1008013167140753413 -filter:videos -filter:retweets -filter:images'
query1 = 'https://twitter.com/FoxNews/status/1007597853802487808 -filter:videos -filter:retweets -filter:images'
query2 = 'https://twitter.com/cnnbrk/status/1006473764018835457 -filter:videos -filter:retweets -filter:images'
query3 = 'https://twitter.com/cnnbrk/status/1006473156868091904 -filter:videos -filter:retweets -filter:images'
query4 = 'https://twitter.com/cnnbrk/status/1006454182596042752 -filter:videos -filter:retweets -filter:images'

query5 = 'https://twitter.com/cnnbrk/status/1006473764018835457 -filter:videos -filter:retweets -filter:images'
query6 = 'https://twitter.com/cnnbrk/status/1006708707554676736 -filter:videos -filter:retweets -filter:images'
query7 = 'https://twitter.com/cnnbrk/status/1006473764018835457 -filter:videos -filter:retweets -filter:images'
query8 = 'https://twitter.com/cnnbrk/status/1006473156868091904 -filter:videos -filter:retweets -filter:images'
query9 = 'https://twitter.com/cnnbrk/status/1006454182596042752 -filter:videos -filter:retweets -filter:images'


#Initialisation of appropriate lists. One for Files one for Queries. 
file_list = ['article.csv','article1.csv','article2.csv','article3.csv','article4.csv','article5.csv','article6.csv','article7.csv','article8.csv','article9.csv']
query_list = [query,query1,query2,query3,query4,query5,query6,query7,query8,query9]


#Loop that calls the API call, opens a file, puts the file into a csv writer, and writes the appropriate data. 
for index in range(0,10):
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query_list[index],lang='en',tweet_mode='extended').items(max_tweets)]
	file = open(file_list[index],'w')
	csvwriter = csv.writer(file)
	outtweets = [[tweet.full_text.encode("utf-8")] for tweet in searched_tweets]
	for item in outtweets:
		csvwriter.writerows(outtweets)
	index+=1




