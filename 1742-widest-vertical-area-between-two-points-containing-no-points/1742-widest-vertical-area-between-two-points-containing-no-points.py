class Solution:
    def maxWidthOfVerticalArea(self, points):
        # まず x 座標だけ取り出す
        x_coords = [x for x, y in points]

        # 昇順に並べる
        x_coords.sort()

        # 最大の差を探す（隣同士の差）
        max_width = 0
        for i in range(1, len(x_coords)):
            # 今までで一番幅が広い区間を記録していく
            max_width = max(max_width, x_coords[i] - x_coords[i - 1])

        return max_width