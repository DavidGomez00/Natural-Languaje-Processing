import math, collections

class KneserNeyLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # Initial values
    self.d=2
    self.total = 0

    # Initiate dicts
    self.bigramsCount = collections.defaultdict(int)
    self.unigramCount = collections.defaultdict(int)
    self.nNextCounts = collections.defaultdict(int)
    self.nPrevCounts = collections.defaultdict(set)

    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  

    # For each sentence
    for sentence in corpus.corpus:
      # Reset the previous token
      prevToken = ""
      # For each word
      for i in range(0, sentence.data):
        # Token
        token = sentence.data[i].word
        # Compute N
        self.total += 1
        # c(w)
        self.unigramCount[token] += 1

        if i > 0:
          prevToken = sentence.data[i - 1].word

          # Count the number of word types prev|next w
          self.nNextCounts[prevToken] += 1
          self.nPrevCounts[token].add(prevToken)
          # Count the number of bigrams
          self.bigramsCount[(token, prevToken)] += 1

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # Initial score
    score = 0.0

    # For each word
    for i in range(1, len(sentence)):
      
      token = sentence[i]
      prevToken = sentence[i - 1]

      # Compute score
      numerator = max(self.bigramsCount[(token, prevToken)] - self.d, 0) + self.d * self.nNextCounts[prevToken] * len(self.nPrevCounts[token]) / len(self.bigramsCount)
        
      if numerator > 0:
          score += math.log(numerator/self.unigramCount[prevToken])
      else:
          score += math.log((self.unigramCount[token] + 1) / (self.total + len(self.unigramCount)))   

    return score
