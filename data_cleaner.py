import csv
import re
import string
import emoji
import time

#Deemojizes a line using regular expression patterns. 
def deemojize_regex(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

#Optional method to deemojize a line in file. 
#Compares each character against a list of unicode emojis. 
def deemojize_(line):
    i = 0
    str1 = list(line) #converts the string into a list.
    str2 = []
    for c in str1: #If character is emoji, skip iteration.
        if c in emoji.UNICODE_EMOJI:
            i+=1
            continue
        else: #otherwise, append into a list.
            str2.append(c)  
        i+=1
    str2 = ''.join(str2) #convert list back into a string.
    return str2    

#List of articles that are cleaned by this script. 
file_list_read = ['article.csv','article1.csv','article2.csv','article3.csv','article4.csv','article5.csv','article6.csv','article7.csv','article8.csv','article9.csv']
file_list_write = ['article_clean.csv','article1_clean.csv','article2_clean.csv','article3_clean.csv','article4_clean.csv','article5_clean.csv','article6_clean.csv','article7_clean.csv','article8_clean.csv','article9_clean.csv']


for index in range(0,10):
    start = time.time()
    listLines = []
    file_read = open(file_list_read[index],'r') #open file for reading
    file_write = open(file_list_write[index],'w') #open file for writing.
    
    #All tweets have their urls, mentions, emojis and punctuation removed. 
    for line in file_read: #for every line in file we read.
        if line in listLines:  #if line is in array skip
            continue
        else:
            listLines.append(line) #otherwise append the from reading file to array.
    
    #now our array is full of unduplicated data. Wrtie this data into our file.
    for line in listLines: #for every line in the array of not duplicate lines.
        result = re.sub(r"http\S+", "", line) #regex to get rid of url.
        result = re.sub(r'[^\w\s]','',result) #regex for punctuation. 
        result = re.sub(r"(?:\@|https?\://)\S+", "", result) #regex for mentions.
        result = deemojize_regex(result) #deemojizes a line.
        result = result.lower() #turns every line into lowercase text.
        file_write.write(result)
        
    file_write.close()
    file_read.close()


