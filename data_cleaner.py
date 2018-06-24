import csv
import re
import string
import timeit


#List of articles that are cleaned by this script. 
file_list_read = ['article.csv','article1.csv','article2.csv','article3.csv','article5.csv','article6.csv','article7.csv','article8.csv']
file_list_write = ['article_clean.csv','article1_clean.csv','article2_clean.csv','article3_clean.csv','article5_clean.csv','article6_clean.csv','article7_clean.csv','article8_clean.csv']


#variables for counting the words.
word_count = 0
iteration_count = 0


for index in range(0,8):
	listLines = []
	file_read = open(file_list_read[index],'r')
	file_write = open(file_list_write[index],'w')

	#All tweets have their urls, mentions and punctuation removed. 
	for line in file_read:
		result = re.sub(r"http\S+", "", line) #regex to get rid of url
		result = result[2:]
		result = re.sub(r'[^\w\s]','',result) #regex for punctuation. 
		result = re.sub(r"(?:\@|https?\://)\S+", "", result) #regex for mentions.

		#this part removes the duplicate data.
		#If the cleaned line is in the array, skip iteration. If not, write to file. 
		if result in listLines: 
			continue
		else:
			file_write.write(result)
			listLines.append(result)
			count = len(re.findall(r'\w+', result))
			word_count+=count
			iteration_count+=count
	print("Number of words in iteration is ",iteration_count)
	iteration_count = 0        
	file_write.close()
	file_read.close()

print("The total amount of words is ",word_count)	





