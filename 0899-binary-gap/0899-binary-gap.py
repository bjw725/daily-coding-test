class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]  # n を 2進数に変換（"0b..." を除く）
        prev = -1
        max_gap = 0
        
        for i, bit in enumerate(binary):
            if bit == '1':
                if prev != -1:
                    max_gap = max(max_gap, i - prev)
                prev = i
        
        return max_gap