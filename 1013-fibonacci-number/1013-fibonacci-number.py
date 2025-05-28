class Solution(object):
    def fib(self, n):

        # ベースケース：n が 0 または 1 のときはそのまま返す
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # 初期値（F(0), F(1)）
        a, b = 0, 1

        # F(2) から F(n) まで計算
        for _ in range(2, n + 1):
            a, b = b, a + b  # a: F(n-2), b: F(n-1)

        # 最後の b が F(n)
        return b