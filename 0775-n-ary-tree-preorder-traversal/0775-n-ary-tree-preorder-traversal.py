class Solution(object):
    def preorder(self, root):

        # 結果を入れるリスト
        result = []

        # 再帰関数で木をたどる
        def dfs(node):
            if not node:
                return
            
            # まずは自分の値を追加（前順の「根」）
            result.append(node.val)

            # そのあとで子ノードたちを左から順に処理
            for child in node.children:
                dfs(child)

        # ルートから探索スタート
        dfs(root)
        return result