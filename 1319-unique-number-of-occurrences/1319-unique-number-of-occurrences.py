class Solution:
    def uniqueOccurrences(self, arr):
        from collections import Counter
        
        freq = Counter(arr).values()
        return len(freq) == len(set(freq))