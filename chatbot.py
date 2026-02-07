# Importing required libraries
import numpy as np #for numerical computation - extremely popular for Data Science
import nltk #for Natural Language Processing
import string #process and handle strings
import random

f = open('C:/Users/FAF Chaudhary/Documents/My Projects/chatbot/chatbot.txt', 'r', encoding = 'utf-8', errors = 'ignore') #f is now a file object, more like a connection or pointer to the file
raw_doc = f.read() #raw_doc is now a string with all the text from the file
raw_doc = raw_doc.lower() #Converts text to lowercase
nltk.download('punkt_tab') #Using the Punkt tokenizer
nltk.download('wordnet') #Using the WordNet Dictionay 
sent_tokens = nltk.sent_tokenize(raw_doc) #Converts doc to list of sentences
word_tokens = nltk.word_tokenize(raw_doc) #Converts doc to list of words

