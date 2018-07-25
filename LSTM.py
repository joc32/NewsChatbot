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
from gensim.models import KeyedVectors
import gensim.models.keyedvectors as word2vec
from keras.models import Model

#load w2v data from pickle module. 
file_read = open('vectors.pkl','rb')
vectors = pickle.load(file_read) #and read it into a variable.
train_x = vectors[0]
train_y = vectors[1]

#now import the actual model. 
word_model = word2vec.KeyedVectors.load_word2vec_format('mymodel')

#Linked with LSTM.
pretrained_weights = word_model.wv.syn0
vocab_size, emdedding_size = pretrained_weights.shape


#Train Long Short Term Memory network with various parameters. 
print('\nTraining LSTM...')
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=emdedding_size, weights=[pretrained_weights]))
model.add(LSTM(units=emdedding_size))
model.add(Dense(units=vocab_size))
model.add(Activation('softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

def word2idx(word):

  return word_model.wv.vocab[word].index

#This method is only used in the generate next lstm part. Not used before fitting the model.  
def idx2word(idx):
  
  return word_model.wv.index2word[idx]


def sample(preds, temperature=1.0):
  if temperature <= 0:
    return np.argmax(preds)
  preds = np.asarray(preds).astype('float64')
  preds = np.log(preds) / temperature
  exp_preds = np.exp(preds)
  preds = exp_preds / np.sum(exp_preds)
  probas = np.random.multinomial(1, preds, 1)
  return np.argmax(probas)

#Second function to be called on callback. 
def generate_next(text, num_generated=10):

  #Generate word2vec indexes for every word and store that in word_idxs. 
  word_idxs = [word2idx(word) for word in text.lower().split()]

  for i in range(num_generated):
    prediction = new_model.predict(x=np.array(word_idxs))
    idx = sample(prediction[-1], temperature=0.7)
    word_idxs.append(idx)

  return ' '.join(idx2word(idx) for idx in word_idxs)

#First function to be called on callback.

def on_epoch_end(epoch):
  print('\nGenerating text after epoch: 20')

  #Seed into the LSTM.
  texts = [
    'We describe a general',
    'deep convolutional',
  ]
  #for every word. Generate text for every word in the texts array.
  for text in texts:
    #and store it in sample.
    sample = generate_next(text)
    print('%s... -> %s' % (text, sample))

#Create the actual models. When the epoch is finished it will call the function on epoch end.   
filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

#Create the LSTM model with the preprocessed data, create 20 epochs, and save them to the local directory.
model.fit(train_x, train_y, batch_size=128, epochs=20, callbacks=callbacks_list)


new_model = load_model('weights-improvement-20-0.0039.hdf5')

#use the model
on_epoch_end(new_model)
