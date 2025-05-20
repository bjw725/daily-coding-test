class Solution:
    def countPairs(self, nums, target):
        count = 0
        n = len(nums)

        # 全ての (i, j) の組み合わせを調べる
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    count += 1  # 条件を満たしたらカウントアップ

        return count