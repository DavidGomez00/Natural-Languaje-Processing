import collections
import math


class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.bigramsCount = collections.defaultdict(int)
    self.unigramCount = collections.defaultdict(int)
    
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus:
      prevToken = ""
      for word in sentence.data:
        token = word.word
        
        #if  token != "</s>":
        self.unigramCount[token] += 1

        #if token != "<s>" and token != "</s>":
        if prevToken != "":
          self.bigramsCount[(token, prevToken)] += 1
        
        prevToken = token
    pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0
    prevToken = ""

    for token in sentence:
      if prevToken != "":
        count = self.bigramsCount[(token, prevToken)] + 1
        score += math.log(count / (self.unigramCount[prevToken] + len(self.bigramsCount)))
      prevToken = token
    return score
