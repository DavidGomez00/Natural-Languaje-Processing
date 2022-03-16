import nltk
import urllib
from urllib import request

url = "http://norvig.com/ngrams/spell-errors.txt"

response =request.urlopen(url)
corpus = response.read().decode('utf8')

tokens = nltk.word_tokenize(corpus)

def deletion(x, w):
    '''def[x, y]: count(xy typed as x)'''
