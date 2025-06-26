class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 小さい順に並べて、負の数から優先的に反転
        nums.sort()

        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1

        # まだ反転が残っている場合は最小値を反転（偶数回ならそのまま）
        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]

        return sum(nums)
        