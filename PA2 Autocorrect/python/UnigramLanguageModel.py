import math, collections

"""Implement a UnigramLanguageModel
   see the UniformLanguage Model as an idea how the data is accessed.
"""


class UnigramLanguageModel:

  def __init__(self, corpus):
    self.unigramCounts = collections.defaultdict(lambda: 0)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """Takes a HolbrookCorpus corpus, does whatever training is needed."""
    # TODO: Train on each word
    pass

  def score(self, sentence):
    """Takes a list of strings, returns a score of that sentence."""
    score = 0.0
    # TODO: Score sentence

    return score
