import math, collections


class LaplaceUnigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # Initialize structures
    self.unigramCounts = collections.defaultdict(lambda: 0)
    # N
    self.total = 0
    # Train
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # For each sentence
    for sentence in corpus.corpus:
      # For each word
      for datum in sentence.data:  
        # Token
        token = datum.word
        # Exclude <s> and </s>
        if token != "<s>" and token != "</s>":
          # c(w) ++
          self.unigramCounts[token] +=  1
          # N ++
          self.total += 1

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # Initial score
    score = 0.0
    # For each word
    for token in sentence:
      # Compute score
      count = self.unigramCounts[token] + 1
      score += math.log(count/(self.total+len(self.unigramCounts)))
    return score
