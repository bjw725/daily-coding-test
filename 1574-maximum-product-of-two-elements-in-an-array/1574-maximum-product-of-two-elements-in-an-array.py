class Solution:
    def maxProduct(self, nums):
        # 大きい順にソートして、上位2つを取る
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)