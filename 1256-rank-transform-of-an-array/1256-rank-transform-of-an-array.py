class Solution:
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(set(arr))
        rank = {num: i + 1 for i, num in enumerate(sorted_unique)}
        return [rank[num] for num in arr]