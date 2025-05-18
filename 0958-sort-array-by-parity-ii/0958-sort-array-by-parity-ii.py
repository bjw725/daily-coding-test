class Solution:
    def sortArrayByParityII(self, nums):
        n = len(nums)

        # 結果を入れる用の配列を先に作っておく
        res = [0] * n

        # 偶数を入れる場所（0番、2番…）
        even = 0

        # 奇数を入れる場所（1番、3番…）
        odd = 1

        # 元の配列を1個ずつ見ていって振り分ける
        for num in nums:
            if num % 2 == 0:
                # 偶数だったら偶数の場所に入れる
                res[even] = num
                even += 2
            else:
                # 奇数だったら奇数の場所に入れる
                res[odd] = num
                odd += 2

        # 最後に結果を返すだけ
        return res