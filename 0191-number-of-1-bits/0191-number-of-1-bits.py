class Solution(object):
    def hammingWeight(self, n):

        # カウント用の変数を用意（1の数を数えていく）
        count = 0

        # nが0になるまでループ
        while n:
            # nの最下位ビットが1ならカウントを増やす
            count += n & 1

            # 右に1ビットずらして、次のビットをチェックする
            n >>= 1

        # 最終的な1の個数を返す
        return count