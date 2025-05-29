from collections import deque

# TreeNodeクラス（LeetCodeでは自動で用意されている）
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        # 結果を入れるリスト
        result = []

        # キューを使って幅優先探索（BFS）を行う
        queue = deque([root])

        # キューが空になるまで繰り返す
        while queue:
            level_size = len(queue)  # このレベルにあるノードの数
            level_sum = 0            # このレベルの値の合計

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                # 子ノードをキューに追加
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 平均値を計算して結果に追加（小数で返す）
            result.append(level_sum * 1.0 / level_size)

        return result