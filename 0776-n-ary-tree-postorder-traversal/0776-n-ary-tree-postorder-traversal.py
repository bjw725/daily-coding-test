class Solution(object):
    def postorder(self, root):
        
        # 結果を格納するリスト
        result = []

        # 再帰関数
        def dfs(node):
            if not node:
                return

            # すべての子ノードを順に処理
            for child in node.children:
                dfs(child)

            # 子を全部見終わったら、最後に自分の値を追加
            result.append(node.val)

        # rootから開始
        dfs(root)
        return result