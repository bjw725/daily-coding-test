class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # 結果を入れていくリストを用意
        res = []

        # 深さ優先探索（DFS）で前順にノードをたどっていく関数を定義
        def dfs(node):
            # ノードが空だったら何もしないで戻る
            if not node:
                return
            
            # まずは今いるノードの値を追加（preorderは根→左→右の順）
            res.append(node.val)
            
            # 左の子ノードを再帰的に処理
            dfs(node.left)
            
            # 右の子ノードも再帰的に処理
            dfs(node.right)

        # rootから探索スタート
        dfs(root)

        # 最後に答えを返す
        return res   