# Importing required libraries
import numpy as np #for numerical computation - extremely popular for Data Science
import nltk #for Natural Language Processing
import string #process and handle strings
import random
import warnings
warnings.filterwarnings('ignore')

f = open('C:/Users/FAF Chaudhary/Documents/My Projects/chatbot/chatbot.txt', 'r', encoding = 'utf-8', errors = 'ignore') #f is now a file object, more like a connection or pointer to the file
raw_doc = f.read() #raw_doc is now a string with all the text from the file
raw_doc = raw_doc.lower() #Converts text to lowercase
nltk.download('punkt_tab') #Using the Punkt tokenizer
nltk.download('wordnet') #Using the WordNet Dictionay 
sent_tokens = nltk.sent_tokenize(raw_doc) #Converts doc to list of sentences
word_tokens = nltk.word_tokenize(raw_doc) #Converts doc to list of words

lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK
def LemToken(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation) 
# it's creating a translation dictionary that maps punctuation characters to None (which means "delete them")
def LemNormalize(text):
    return LemToken(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    #translate() is a string method that uses the dictionary you created to transform the text, in this case, to remove punctuation.

GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREET_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greet(sentence):
    
    for word in sentence.split():
        if word.lower() in GREET_INPUTS :
            return random.choice(GREET_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#TfidfVectorizer converts text into numbers that represent how important each word is

#Function that takes the user's input as a parameter
def response(user_response):
    robo1_response = '' #Empty string to store the chatbot's response
    #clean and lemmatize words and ignore stop words
    TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english')
    #Converts ALL sentences in your chatbot.txt (stored in sent_tokens) into TF-IDF number vectors
    tfidf = TfidfVec.fit_transform(sent_tokens)
    #Compares the last sentence in sent_tokens (which is the user's input - added earlier in the code) to all sentences.
    vals = cosine_similarity(tfidf[-1], tfidf)
    #vals.argsort() = sorts similarity scores and returns their indices (positions)
    #[0] = gets the first row
    #[-2] = gets the second-to-last index
    idx = vals.argsort()[0][-2]
    flat = vals.flatten() #Converts the 2D array of similarity scores into a 1D array
    flat.sort() #Sorts all similarity scores from lowest to highest
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo1_response = robo1_response + "I am sorry! I don't understand you"
        return robo1_response
    else:
        robo1_response = robo1_response +sent_tokens[idx]
        
    sent_tokens.remove(user_response)
    return robo1_response
    
flag = True
print("BOT: My name is Fami. Let's have a conversation! Also, if you want to exit any time, just type Bye!")
while (flag == True):
    user_response = input("You: ")
    user_response = user_response.lower()
    if(user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            print("BOT: You are welcome..")
        else:
            if (greet(user_response) != None):
                print("BOT: " +greet(user_response))
            else:
                sent_tokens.append(user_response)
                word_tokens = word_tokens + nltk.word_tokenize(user_response)
                final_words = list(set(word_tokens))
                print("BOT: ", end = "")
                print(response(user_response))
    else:
        flag = False
        print("BOT: Goodbye! ")