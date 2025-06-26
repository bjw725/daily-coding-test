class Solution:
    def isAlienSorted(self, words, order):
        order_map = {char: i for i, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c1, c2 in zip(w1, w2):
                if order_map[c1] < order_map[c2]:
                    break
                elif order_map[c1] > order_map[c2]:
                    return False
            else:
                if len(w1) > len(w2):
                    return False
        return True