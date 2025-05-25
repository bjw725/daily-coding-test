class Solution(object):
    def reverseString(self, s):

        # 両端からポインタを使って交換していく
        left, right = 0, len(s) - 1

        # ポインタがぶつかるまで繰り返す
        while left < right:
            # 左右の文字を入れ替え
            s[left], s[right] = s[right], s[left]

            # ポインタを内側に一つずつ進める
            left += 1
            right -= 1