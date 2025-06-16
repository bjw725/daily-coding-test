class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1
        current_width = 0

        for char in s:
            w = widths[ord(char) - ord('a')]
            if current_width + w > 100:
                lines += 1
                current_width = w  # 新しい行で最初の文字
            else:
                current_width += w

        return [lines, current_width]