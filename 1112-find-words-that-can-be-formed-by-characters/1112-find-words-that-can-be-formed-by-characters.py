class Solution:
    def countCharacters(self, words, chars):
        from collections import Counter
        
        chars_count = Counter(chars)
        total = 0
        
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= chars_count[c] for c in word_count):
                total += len(word)
        
        return total