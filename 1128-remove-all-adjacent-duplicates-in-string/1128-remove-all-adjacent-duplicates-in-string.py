class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # 隣接かつ同じ → 削除
            else:
                stack.append(char)

        return ''.join(stack)