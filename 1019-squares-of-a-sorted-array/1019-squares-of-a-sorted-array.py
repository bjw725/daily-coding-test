class Solution:
    def sortedSquares(self, nums):
        # 全部2乗してからソート
        return sorted(x * x for x in nums)