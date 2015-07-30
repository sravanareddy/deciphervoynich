from __future__ import division
from collections import Counter, defaultdict
import codecs
from math import log
import string

def log2(n):
    return log(n, 2)

def build_unigrams(wordlist):
    unigrams = Counter(wordlist)
    for word in unigrams:
        unigrams[word]/=len(wordlist)
    return unigrams

def entropy(dist):
    return 0 - sum(map(lambda prob: prob*log2(prob), dist.values()))

class CorpusStats:
    def __init__(self, rawtext):
        self.rawtext = rawtext
        self.chartypes = set(self.rawtext).difference(set(string.whitespace))
        
        self.tokens = self.rawtext.split()
        self.numtokens = len(self.tokens)
        self.types = set(self.tokens)
        self.numtypes = len(self.types)
        
    def count_wordlengths(self):
        """Count word length distribution over types and tokens (sec 4.1, figure 3)"""
        tokenlens = map(lambda word: len(word), self.tokens)
        tokenlens_dist = Counter(tokenlens)
        for length in tokenlens_dist:
            tokenlens_dist[length]/=self.numtokens 
        
        typelens = map(lambda word: len(word), self.types)
        typelens_dist = Counter(typelens)
        for length in typelens_dist:
            typelens_dist[length]/=self.numtypes
        return tokenlens_dist, typelens_dist

    def compute_unigram_entropy(self):
        """Shannon entropy of unigram distribution (sec 4.1, table 1)"""
        return entropy(build_unigrams(self.tokens))

    def get_bestsub(self):
        """for each character, find alternate character d such that subsituting d for c in the whole corpus produces max reduction in word entropy (sec 3.2)"""
        pairwise_entdec = {}
        chartypelist = list(self.chartypes)
        for ci, c in enumerate(chartypelist):
            for d in chartypelist[ci+1:]:
                wordlist = filter(lambda word: c in word or d in word, self.tokens)
                myent = entropy(build_unigrams(wordlist))
                pairwise_entdec[(c, d)] = myent - entropy(build_unigrams(map(lambda word: word.replace(c, d), wordlist)))
        bestsub = defaultdict(lambda : ('', 0))
        for (c, d), score in pairwise_entdec.items():
            if score > bestsub[c][1]:
                bestsub[c] = (d, score)
            if score > bestsub[d][1]:
                bestsub[d] = (c, score)
        return bestsub

if __name__=='__main__':
    voynichb = CorpusStats(codecs.open('data/voy.b.paged.wds', 'r', 'utf8').read())
