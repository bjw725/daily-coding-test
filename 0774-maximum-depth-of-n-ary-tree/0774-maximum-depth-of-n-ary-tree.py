class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        
        # 各子ノードの最大深さを再帰的に計算し、その中で最大のものに1を加える
        return 1 + max(self.maxDepth(child) for child in root.children)