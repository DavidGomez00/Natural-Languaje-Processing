import collections
import math

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    
    # Initialize structures
    self.bigramsCount = collections.defaultdict(int)
    self.unigramCount = collections.defaultdict(int)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """
    
    for sentence in corpus.corpus:
      # Add unicgramCounts for the first word
      self.unigramCount[sentence[0]] += 1
      # loop for the rest
      for i in range(1, len(sentence.data)):
        # Assign tokens
        token = sentence[i]
        prevToken = sentence[i-1]
        
        self.unigramCount[token] += 1
        self.bigramsCount[(token, prevToken)] += 1
        self.total += 1

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """

    # Initial score
    score = 0.0

    # loop for each bigram
    for i in range(1, sentence):
      token = sentence[i]
      prevToken = sentence[i-1]

      if self.bigramsCount[(token, prevToken)] > 0:

        count = self.bigramsCount[(token, prevToken)]
        score += math.log(count / (self.unigramCount[prevToken]))
    else:

        count = self.unigramCount[token] + 1
        score += math.log(0.4 * count / (self.total + len(self.unigramCount)))
        
    return score
