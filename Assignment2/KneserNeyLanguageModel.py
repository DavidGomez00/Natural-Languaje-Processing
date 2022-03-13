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

    # For each sentence
    for sentence in corpus.corpus:
      # Counts for the first token in the sentence
      self.unigramCount[sentence.data[0].word] += 1
      self.unigrams.add(sentence.data[0].word)
      self.total += 1

      # For each word
      for i in range(1, len(sentence.data)):
        # Token
        token = sentence.data[i].word
        prevToken = sentence.data[i - 1].word

        # Compute N
        self.total += 1

        # c(w)
        self.unigramCount[token] += 1
        self.unigrams.add(token)

        # Count the number of word types prev|next w
        self.nNextCounts[prevToken] += 1
        self.nPrevCounts[token].add(prevToken)

        # Count the number of bigrams
        self.bigramsCount[(token, prevToken)] += 1
        self.bigrams.add((token, prevToken))

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
      numerator = max(self.bigramsCount[(token, prevToken)] - self.d, 0) + self.d * self.nNextCounts[prevToken] * len(self.nPrevCounts[token]) / len(self.bigrams)
      
      if numerator > 0:
          score += math.log(numerator/self.unigramCount[prevToken])
      else:
          score += math.log((self.unigramCount[token] + 1) / (self.total + len(self.unigrams)))   

    return score
