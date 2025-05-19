class Solution:
    def maxProductDifference(self, nums):
        # まず小さい順に並べる
        nums.sort()

        # 最大のペア：一番大きい2つ
        max_product = nums[-1] * nums[-2]

        # 最小のペア：一番小さい2つ
        min_product = nums[0] * nums[1]

        # 差を返す
        return max_product - min_product