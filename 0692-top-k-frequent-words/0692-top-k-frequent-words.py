import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)

        # Sort by:
        # 1. Frequency descending
        # 2. Word lexicographically ascending
        words_list = list(count.keys())

        words_list.sort(key=lambda word: (-count[word], word))

        return words_list[:k]