from collections import Counter

class Solution:
    def frequencySort(self, nums):
        # 値ごとの出現回数を数える（頻度）
        freq = Counter(nums)

        # 頻度が小さい順、値は大きい順にソート
        nums.sort(key=lambda x: (freq[x], -x))

        return nums