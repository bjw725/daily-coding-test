class Solution(object):
    def judgeCircle(self, moves):

        # 現在位置を追跡（xが左右、yが上下）
        x, y = 0, 0

        # 各移動を順に処理
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1

        # 最終的な位置が原点ならTrue
        return x == 0 and y == 0