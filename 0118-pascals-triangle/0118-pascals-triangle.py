class Solution(object):
    def generate(self, numRows):
        # 結果を入れるリスト
        result = []

        # 各行を1つずつ作っていく
        for i in range(numRows):
            # 行の最初は1でスタート
            row = [1] * (i + 1)

            # 中身は、上の行の左右の値を足し合わせたものになる
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            # 出来た行を結果に追加
            result.append(row)

        return result