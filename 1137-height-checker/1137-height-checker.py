class Solution:
    def heightChecker(self, heights):
        # heights を昇順に並べて「正しい並び」を作る
        expected = sorted(heights)

        count = 0  # ずれてる場所の数をカウント

        # 現在の並びと正しい並びを1個ずつ比べていく
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1  # もし違ってたらカウントアップ

        return count