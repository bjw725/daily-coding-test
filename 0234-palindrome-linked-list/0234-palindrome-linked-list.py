class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # ステップ 1: 全ノードの値をリストに格納
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        # ステップ 2: リストが回文かどうかを判定
        return vals == vals[::-1]