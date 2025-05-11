class Solution(object):
    def findMaxK(self, nums):
        seen = set(nums)
        max_k = -1
        for num in nums:
            if -num in seen and num > 0:
                max_k = max(max_k, num)
        return max_k