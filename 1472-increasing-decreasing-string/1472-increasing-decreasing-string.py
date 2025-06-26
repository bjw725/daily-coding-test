class Solution:
    def sortString(self, s):
        from collections import Counter
        
        count = Counter(s)
        result = []
        
        while len(result) < len(s):
            # Ascending pass
            for ch in sorted(count.keys()):
                if count[ch] > 0:
                    result.append(ch)
                    count[ch] -= 1
            # Descending pass
            for ch in sorted(count.keys(), reverse=True):
                if count[ch] > 0:
                    result.append(ch)
                    count[ch] -= 1
        
        return ''.join(result)