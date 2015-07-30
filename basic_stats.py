from __future__ import division
from collections import Counter
import codecs

def count_wordlengths(filename):
    """Count word length distribution over types and tokens"""
    tokens = codecs.open(filename, 'r', 'utf8').read().split()
    tokenlens = map(lambda word: len(word), tokens)
    tokenlens_dist = Counter(tokenlens)
    for length in tokenlens_dist:
        tokenlens_dist[length]/=len(tokens) #normalized count distribution
    types = set(tokens)
    typelens = map(lambda word: len(word), types)
    typelens_dist = Counter(typelens)
    for length in typelens_dist:
        typelens_dist[length]/=len(types)
    return tokenlens_dist, typelens_dist

