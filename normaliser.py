import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


#Required corpi for data processing.
# nltk.download('punkt')
# nltk.download('wordnet')


file_read = open('article3_clean.txt','r')
file_write = open('Normalised3.txt','w')



lmtzr = WordNetLemmatizer() #Instantiates new lemmatiser object. 
stemmer = PorterStemmer() #Instantiates new stemming object. 


#Normalises each word. 
for line in file_read:
	words = nltk.word_tokenize(line) #splits the line into individual words / tokens
	for item in words:
		item = lmtzr.lemmatize(item) #Lemmatizes every word
		item = stemmer.stem(item)    #stemms every word
		file_write.write(item)
		file_write.write(' ')
