import nltk
from nltk.corpus import brown
import random

# FreqDist of all words
all_words = nltk.FreqDist(w.lower() for w in brown.words())
# Take 2000 more common
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

documents = [(list(brown.words(fileid)), category) 
            for category in brown.categories() 
            for fileid in brown.fileids(category)]

random.shuffle(documents)

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]

classifier = nltk.NaiveBayesClassifier.train(train_set)

classifier.show_most_informative_features(100)
