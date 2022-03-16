import collections
import math


class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    
    # Initialize structures
    self.bigramsCount = collections.defaultdict(int)
    self.unigramCount = collections.defaultdict(int)

    # Initialize sets
    self.words = set()

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
            self.words.add(token)
        
        i += 1


  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """

    # Initial score
    score = 0.0

    # For each word
    for i in range(1, len(sentence)):
      
      # Assing tokens
      token = sentence[i]
      prevToken = sentence[i-1]

      # Compute score
      count = self.bigramsCount[(prevToken, token)] + 1
      score += math.log(count / (self.unigramCount[prevToken] + len(self.words)))

    return score
