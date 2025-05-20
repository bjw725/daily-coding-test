class Solution:
    def transformArray(self, nums):
        # 偶数は0、奇数は1に変換
        binary = [0 if x % 2 == 0 else 1 for x in nums]

        # 昇順に並べる
        binary.sort()

        return binary