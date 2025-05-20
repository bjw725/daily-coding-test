class Solution(object):
    def deleteGreatestValue(self, grid):

        # 各行をソート（降順）して、最大値を先頭に
        for row in grid:
            row.sort(reverse=True)
        
        result = 0
        # 各列ごとに最大値を取る
        for col in range(len(grid[0])):
            max_in_col = max(row[col] for row in grid)
            result += max_in_col
        
        return result