from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)  # 各文字の出現回数をカウント

        for i, char in enumerate(s):
            if count[char] == 1:
                return i  # 最初に1回しか出現しない文字のインデックスを返す

        return -1  # 該当する文字がない場合