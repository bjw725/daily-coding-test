class Solution:
    def sortByBits(self, arr):
        # ソートする時のキーを「1の数 → 値の順」で設定
        # bin(x)で2進数にして、'1'の数をカウント
        arr.sort(key=lambda x: (bin(x).count('1'), x))
        return arr