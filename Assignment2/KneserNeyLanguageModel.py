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

    # Initialize sets
    self.bigrams = set()
    self.unigrams = set()

    # Train
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  

    for sentence in corpus.corpus:
      # position in the sentence
      i = 0

      # For each word
      for datum in sentence.data:  
        # Token
        token = datum.word
        self.unigramCount[token] += 1
      
        # Exists a previous token
        if i > 0:
          # Assign prevToken
          prevToken = sentence.data[i - 1].word

          # Count bigrams
          self.bigramsCount[(prevToken, token)] += 1
          self.bigrams.add((prevToken, token))

          # Count the number of word types prev|next w
          self.nNextCounts[prevToken] += 1
          self.nPrevCounts[token].add(prevToken)

          if i < len(sentence) - 1:
            self.words.add(token)
            self.total +=1
          
          i += 1

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """

    # Initial score
    score = 0.0

    # For each word
    for i in range(1, len(sentence)):
      # Assign token and prevToken
      token = sentence[i]
      prevToken = sentence[i - 1]

      # Compute score
      numerator = max(self.bigramsCount[(prevToken, token)] - self.d, 0) + self.d * self.nNextCounts[prevToken] * len(self.nPrevCounts[token]) / len(self.bigrams)
      
      if numerator > 0:
          score += math.log(numerator/self.unigramCount[prevToken])
      else:
          score += math.log((self.unigramCount[token] + 1) / (self.total + len(self.unigrams)))   

    return score
