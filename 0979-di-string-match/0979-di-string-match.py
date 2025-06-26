class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        low, high = 0, n
        res = []

        for char in s:
            if char == 'I':
                res.append(low)
                low += 1
            else:  # char == 'D'
                res.append(high)
                high -= 1

        # 最後に残った数字を追加（low == high）
        res.append(low)
        return res