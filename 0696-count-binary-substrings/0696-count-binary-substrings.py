class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 0
        curr = 1
        count = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                # 異なる文字に変わった → 部分グループの切り替え
                count += min(prev, curr)
                prev = curr
                curr = 1

        # 最後のグループとの比較も忘れずに加算
        count += min(prev, curr)
        return count