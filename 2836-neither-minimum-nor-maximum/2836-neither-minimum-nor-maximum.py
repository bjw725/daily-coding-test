class Solution(object):
    def findNonMinOrMax(self, nums):
        
        # 要素数が2以下なら、minでもmaxでもない数は存在しない
        if len(nums) <= 2:
            return -1

        # 最小値と最大値を取得
        min_val = min(nums)
        max_val = max(nums)

        # 最小でも最大でもない数を探す
        for num in nums:
            if num != min_val and num != max_val:
                return num

        # 念のための保険（通常はここに来ない）
        return -1