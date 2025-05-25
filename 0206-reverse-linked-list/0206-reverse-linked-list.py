class Solution(object):
    def reverseList(self, head):

        # 反転後のリストの先頭を指す変数（最初は何もないのでNone）
        prev = None

        # 現在のノードをたどるための変数（最初はheadからスタート）
        current = head

        # リストの最後までループして処理していく
        while current:
            # 次のノードを一時的に保存（今のノードのnextをあとで上書きするから）
            next_node = current.next

            # 今のノードのnextを前のノードに付け替え（ここが反転のポイント）
            current.next = prev

            # prevとcurrentを一つ進める（次のステップの準備）
            prev = current
            current = next_node

        # 最後まで処理したら、prevが新しい先頭になってるのでそれを返す
        return prev