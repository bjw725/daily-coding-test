class MyHashSet(object):

    def __init__(self):
        # 初期化：キーの最大値が 10^6 のため、その範囲をカバーできる大きさの配列を使う
        self.size = 10**6 + 1
        self.bucket = [False] * self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.bucket[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.bucket[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.bucket[key]