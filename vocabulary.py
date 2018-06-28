import sys



# Function that takes an input file, blank dictionary
# and returns a dictionary of words with its frequency. 

def dictionary_handler(file_name,my_list):

    file_read = file_name
    wordfreq = my_list

    for line in file_read:
        words = line.split() #Splits the line into words.
        for word in words:
            if word not in wordfreq: #if word not in dict, append a word to the dict and set the count to 1.
                wordfreq[word] = 1
            else:    
                wordfreq[word] += 1 #if word in the dict, increase the count by one
    return wordfreq       


argument = sys.argv[1]

if argument == 'create':
    print('Creating vocaulary')
    wordfreq = {}
    file_read = open('article1_clean.txt','r')
    file_write = open('vocabulary.txt','w') #File that will actually store the dictionary.
    dictionary_handler(file_read,wordfreq)

    # Sort the dictionary by descending order and add the newly created dictionary into the vocabulary txt file. 
    for word in sorted(wordfreq, key=wordfreq.get, reverse=True):
        file_write.write(str(word) + " " + str(wordfreq[word]) + "\n")






