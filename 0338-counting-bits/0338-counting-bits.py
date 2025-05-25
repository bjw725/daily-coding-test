class Solution(object):
    def countBits(self, n):

        # 結果を入れる配列（最初は全部0で初期化）
        ans = [0] * (n + 1)

        # 1から順に、前の結果を使って計算していく
        for i in range(1, n + 1):
            # i >> 1 は i を右に1ビットずらした値（つまり i//2）
            # i & 1 は最下位ビットが1かどうか（1なら奇数）
            ans[i] = ans[i >> 1] + (i & 1)

        # 最終的なリストを返す
        return ans