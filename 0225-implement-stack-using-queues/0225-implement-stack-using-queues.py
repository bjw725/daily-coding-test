from collections import deque

class MyStack(object):

    def __init__(self):
        # 2つのキューを用意（操作のたびに使い分ける）
        self.q1 = deque()  # メインのキュー
        self.q2 = deque()  # 一時的に使うキュー

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 新しい要素はまずq2に追加
        self.q2.append(x)

        # q1にある既存の要素を全部q2に移す（順番を逆にするため）
        while self.q1:
            self.q2.append(self.q1.popleft())

        # q1とq2を入れ替える（q1が常に最新の状態を保つように）
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        :rtype: int
        """
        # q1の先頭がスタックのトップなので、それを取り出す
        return self.q1.popleft()

    def top(self):
        """
        :rtype: int
        """
        # q1の先頭がトップの要素
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        # q1が空かどうかでスタックが空か判断
        return not self.q1