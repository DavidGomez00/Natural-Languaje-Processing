import collections
import math

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    
    # Initialize dicts
    self.bigramsCount = collections.defaultdict(int)
    self.unigramCount = collections.defaultdict(int)

    # Initialize sets
    self.unigrams = set()
    self.bigrams = set()

    # Total words
    self.total = 0

    # Train
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """
    for sentence in corpus.corpus:
      
      i = 0
      # For each word
      for datum in sentence.data:  
        # Token
        token = datum.word
        self.unigramCount[token] += 1
      
        if i > 0:
          prevToken = sentence.data[i - 1].word
          # Count bigrams
          self.bigramsCount[(prevToken, token)] += 1

          if i < len(sentence) - 1:
            self.unigrams.add(token)
            self.total += 1
            
            if  i > 1:
              self.bigrams.add((prevToken, token))
        
        i += 1
        

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """

    # Initial score
    score = 0.0

    # loop for each bigram
    for i in range(1, len(sentence)):
      token = sentence[i]
      prevToken = sentence[i-1]

      if self.bigramsCount[(prevToken, token)] > 0:
        count = self.bigramsCount[(prevToken, token)]
        score += math.log(count / (self.unigramCount[prevToken]))
      else:
        count = self.unigramCount[token] + 1
        score += math.log(0.4 * count / (self.total + len(self.unigrams)))
        
    return score
