# NewsChatbot
News Chatbot with Neural Networks

Development Process

1. Implement a parser that parses data from Twitter using Tweepy. 
2. Clean the data from elements such as tweet's url, mentions, punctuation...
3. Normalise the data by lemmatising and stemming it. 
4. Create a vocabulary of N most frequent words.
5. Create a vector space of entire data from the dictionary using word2vec algorithm.
6. Train LSTM recurrent neural networks with the data. 

Libraries and Technologies Used:

Python - the entire project up to now written in Python 3.6.4.

Tweepy - Parsing the data from Twitter. 
NLTK - Lemmatising, tokenising and stemming the data.
Keras - Training the LSTM Neural Networks.
Numpy - Used for various data procedures. 
