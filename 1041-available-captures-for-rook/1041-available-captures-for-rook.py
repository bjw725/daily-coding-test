class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # ルークの位置を探す
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
        count = 0

        for dx, dy in directions:
            x, y = rook_row + dx, rook_col + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'B':
                    break  # 遮られる
                if board[x][y] == 'p':
                    count += 1  # 攻撃可能
                    break
                x += dx
                y += dy

        return count