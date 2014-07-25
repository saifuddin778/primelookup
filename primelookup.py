from __future__ import division
import sys
sys.dont_write_bytecode = True
import math
__author__ = 'Saifuddin Abdullah'

"""
Primelookup - packed in a single portable object
"""
class primelookup(object):
    """
    init
    """
    def __init__(self, docs):
        #first 26 primes of the form 4n+3 
        #the point is any of these multiplied with any other(s) in any form always produces a unique
        #product..and that product only has those factors which resulted it in the given finite space.
        self.v  = {'a': 7, 'c': 11, 'b': 19, 'e': 23, 'd': 31, 'g': 43, 'f': 47, 'i': 59, 'h': 67, 'k': 71, 'j': 79, 'm': 83, 'l': 103, 'o': 107, 'n': 127, 'q': 131, 'p': 139, 's': 151, 'r': 163, 'u': 167, 't': 179, 'w': 191, 'v': 199, 'y': 211, 'x': 223, 'z': 227}
        self.t = {}
        self.docs = docs

    """
    scoring function
    """
    def score(self, s):
        u = 1
        for a in s:
            u *= self.v[a]
        return (self.v[s[0]]*self.v[s[1]]*self.v[s[2]], self.v[s[int(len(s)/2)]], self.v[s[-1]], u)

    """
    generates mappings...can be huge when large corpus is provided, but
    we can always serialize and memory map it after it is generated, so that
    it can be pre-loaded before querying.
    """
    def map_primes(self):
        for i in range(0, len(self.docs)):
            _id = self.docs[i][0]
            sent_ = self.docs[i][1].split(' ')
            for j in range(0, len(sent_)):
                if len(sent_[j]) > 2:
                    score_vec = self.score(sent_[j])
                    first, middle, last, score  = score_vec
                    if self.t.has_key(first):
                        if self.t[first].has_key(middle):
                            if self.t[first][middle].has_key(last):
                                self.t[first][middle][last].append((_id, score))
                            else:
                                self.t[first][middle][last] = []
                                self.t[first][middle][last].append((_id, score))
                        else:
                            self.t[first][middle] = {}
                            self.t[first][middle][last] = []
                            self.t[first][middle][last].append((_id, score))
                    else:
                        self.t[first] = {}
                        self.t[first][middle] = {}
                        self.t[first][middle][last] = []
                        self.t[first][middle][last].append((_id, score))
        return self.t

    """
    get the closest item within the given table or dict
    """
    def get_closest(self, table_, value, type_):
        if type_== 'dict':
            table = table_.keys()
        elif type_ == 'list':
            table = table_
        current_val = abs(table[0] - value)
        current_item = table[0]
        for i in range(0, len(table)):
            if abs(table[i]  - value) < current_val:
                current_item = table[i]
                current_value = abs(table[i] - value)
        return current_item

    """
    main search method - please note that the lookup time
    is minimum in most of the cases since only 1d subarrays of numerical
    values are looked up..and most of the time (given that the mappings are
    generated on rich corpus), it should be a constant time lookup from
    the hash.
    """
    def search(self, word):
        first, middle, last, score = self.score(word)
        try:
            result = self.t[first][middle][last]
        except:
            if self.t.has_key(first):
                if self.t[first].has_key(middle):
                    last_candidate = self.get_closest(self.t[first][middle], last, 'dict')
                    result = self.t[first][middle][last_candidate]
                else:
                    middle_candidate = self.get_closest(self.t[first], middle, 'dict')
                    last_candidate = self.get_closest(self.t[first][middle_candidate], last, 'dict')
                    result = self.t[first][middle_candidate][last_candidate]
            else:
                #rare case because we will be training with all the alphabetical orders
                first_candidate = self.get_closest(self.t, first, 'dict')
                middle_candidate = self.get_closest(self.t[first_candidate], middle, 'dict')
                last_candidate = self.get_closest(self.t[first_candidate][middle_candidate], last, 'dict')
                result = self.t[first_candidate][middle_candidate][last_candidate]
        return result
