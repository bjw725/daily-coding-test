class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        cells = []

        # 全セルの座標を列挙
        for r in range(rows):
            for c in range(cols):
                cells.append([r, c])

        # マンハッタン距離でソート
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))

        return cells