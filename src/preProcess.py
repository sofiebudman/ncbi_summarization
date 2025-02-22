import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer, WordNetLemmatizer
#from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


#parses the string to just take the stuff starting at abstract
def extractAbstract(pubmedDictionary):
    abstract = pubmedDictionary['Abstract']
    return(abstract)
    return 1 #other functions get whole page, we just want to get the contents of the abstract


#removes all punctuation
def removePunctuation(text):
    out = ""
    punctuation = ['.', ',', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}', '"', "'", '...', '&', '...']
    for c in text:
        if( not c in punctuation):
            out +=c

    return out

#clean text function
def clean(text):
    text = text.lower()  
    text = removePunctuation(text)
    text = removeStopWords(text)
    return text

#removes the stop words
def removeStopWords(text):
    stop_words = set(stopwords.words('english'))
    out = ' '.join([word for word in text.split() if word not in stop_words])
    return out

