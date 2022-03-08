import collections
import math

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.bigramsCount = collections.defaultdict(int)
    self.unigramCount = collections.defaultdict(int)
    self.total = 0
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
        self.total += 1

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

        if self.bigramsCount[(token, prevToken)] > 0:

          count = self.bigramsCount[(token, prevToken)]
          score += math.log(count / (self.unigramCount[prevToken]))
        else:

          count = self.unigramCount[token] + 1
          score += math.log(0.4 * count / (self.total + len(self.unigramCount)))
      
      prevToken = token
    return score
