import collections
import math


class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # Initialize structures
    self.bigramsCount = collections.defaultdict(int)
    self.unigramCount = collections.defaultdict(int)
    self.words = set()
    self.bigrams = set()

    
    # Train
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # For each sentence
    for sentence in corpus.corpus:
      # First word has no previous token
      prevToken = ""

      # For each word
      for i in range(0, len(sentence.data)):
        if i == 0:
          token = sentence.data[i].word

        if i > 0:
          prevToken = sentence.data[i - 1].word
        
          # Token
          token = sentence.data[i].word
          
          # Count bigrams
          self.bigramsCount[(token, prevToken)] += 1
          self.bigrams.add((token, prevToken))

          # Set token as the next previous token
          prevToken = token

        # c(w)
        self.unigramCount[token] += 1
        self.words.add(token)


  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # Initial score
    score = 0.0
    # First word has no previous token
    prevToken = ""

    # For each word
    for token in sentence:
      if prevToken != "":
        # Compute score
        count = self.bigramsCount[(token, prevToken)] + 1
        score += math.log(count / (self.unigramCount[prevToken] + len(self.bigrams)))
      # Set the current token as the next previous token
      prevToken = token
    return score
