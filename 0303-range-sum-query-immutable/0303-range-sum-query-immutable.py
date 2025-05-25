class NumArray(object):

    def __init__(self, nums):
        # 累積和を計算しておく（prefix[i] は nums[0] ~ nums[i-1] の合計）
        self.prefix = [0]

        # 1個ずつ足しながらprefix配列を作っていく
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        # right+1までの合計からleftまでの合計を引くと、ちょうどleft〜rightの和になる
        return self.prefix[right + 1] - self.prefix[left]