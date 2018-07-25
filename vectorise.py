import numpy as np
import gensim
import string
import pickle

from keras.callbacks import LambdaCallback
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.layers import Dense, Activation
from keras.models import Sequential
from keras.utils.data_utils import get_file
from keras.callbacks import ModelCheckpoint
from keras.models import load_model

from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec, KeyedVectors

#Code that creates a vector represtentation of a text corpus. 
# 1. Splits the text corpus into N arrays with K length.
# 2. Vectorises these N arrays
# 3. Prepares the words into a form that is acceptable by a LSTM network.
# 4. Stores the data into a Pickle module for later retreival.

#Open our text data and store into a variable called docs.
with open(path) as file_:
  docs = file_.readlines()

#Length of the sentence. Can be any size. 
max_sentence_len = 40

#Divides the whole text file into tokenised sentences of length 40 with no punctuation.  
sentences = [[word for word in doc.lower().translate(string.punctuation).split()[:max_sentence_len]] for doc in docs]
print('Num sentences:', len(sentences))

print('\nTraining word2vec...')
word_model = gensim.models.Word2Vec(sentences, size=100, min_count=1, window=5, iter=100)

#Saving the model. 
word_model.wv.save_word2vec_format('mymodel')

#linked with LSTM later on.
pretrained_weights = word_model.wv.syn0
vocab_size, emdedding_size = pretrained_weights.shape

#This method basically just returns the index of a word from our already existing word2vec model. 
def word2idx(word):

  return word_model.wv.vocab[word].index

#This method is only used in the generate next lstm part. Not used before fitting the model.  
def idx2word(idx):
  
  return word_model.wv.index2word[idx]

#LSTM Data Preprocessing. The Data has to be fed in a specific format in order to be put into LSTM model creation. 
#Every word gets an numerical value (index) associated to it from the Word2Vec model. Look at word2idx method.
print('\n LSTM Data Preprocessing...')

#We need these two X and Y parameters because they will be then supplied into the LSTM model creation.
# X - training data
# Y - target data. 

#Create arrays filled with zeros of length supplied from senteces array. 
train_x = np.zeros([len(sentences), max_sentence_len], dtype=np.int32) #create an 2d array filled with zeros of dimenssions #7200 x 40.
train_y = np.zeros([len(sentences)], dtype=np.int32) #create an 1d array of zeros with length 7200.

#Get the index of every word and replace the 0 with an actual number.
for i, sentence in enumerate(sentences):
  for t, word in enumerate(sentence[:-1]): #to all elements except the last one. 
    train_x[i, t] = word2idx(word)  
  train_y[i] = word2idx(sentence[-1]) #the last element of each sentence. #So 40th element ... 

#save X and Y arrays to pickle modules for future retrieval. 
file_write = open('vectors.pkl', 'wb')  #store the dictionary into a pickle file, write mode is binary
vectors = [train_x,train_y]
pickle.dump(vectors, file_write)
file_write.close()
