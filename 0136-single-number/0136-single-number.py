class Solution(object):
    def singleNumber(self, nums):
        result = 0

        # 配列の中身を順にXORしていく
        for num in nums:
            result ^= num  # これで同じ数は消えて、1個だけ残る

        return result