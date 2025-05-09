class Solution:
    def intersection(self, nums):
        common = set(nums[0])  # 첫 배열로 시작

        for arr in nums[1:]:
            common &= set(arr)  # 교집합 연산

        return sorted(common)