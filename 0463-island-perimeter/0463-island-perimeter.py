class Solution(object):
    def islandPerimeter(self, grid):

        # グリッドのサイズ
        rows = len(grid)
        cols = len(grid[0])
        
        # 外周の合計をカウントする変数
        perimeter = 0

        # 全てのセルをチェック
        for i in range(rows):
            for j in range(cols):
                # 陸地セルなら
                if grid[i][j] == 1:
                    # 仮に四方すべてが水や外なら +4
                    perimeter += 4

                    # 上に陸地があれば、その辺は共有 → -2
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    # 左に陸地があれば、その辺も共有 → -2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        # 最終的な外周を返す
        return perimeter