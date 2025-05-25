class MyQueue(object):

    def __init__(self):
        # 入力用スタック（新しい要素をpushしていく）
        self.in_stack = []
        # 出力用スタック（pop/peekのときに使う）
        self.out_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 新しい要素はin_stackに追加（後ろに入れるイメージ）
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # out_stackが空ならin_stackから全部移して順序を逆にする
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # 先頭の要素を取り出す
        return self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        # popと同じく、必要ならスタックを移動してからpeek
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # キューの先頭を返す（削除しない）
        return self.out_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # 両方のスタックが空ならキューも空ってこと
        return not self.in_stack and not self.out_stack