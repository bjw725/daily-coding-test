class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # a と b が同じなら、どちらの部分列も両方に存在 → -1
        if a == b:
            return -1
        # 違うなら、長い方の文字列全体が最長の「一方だけの部分列」
        return max(len(a), len(b))