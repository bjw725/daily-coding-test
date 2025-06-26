class MyHashMap(object):

    def __init__(self):
        self.size = 1000  # バケット数（適度に分散するための素数に近い数）
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        # キーが存在するなら更新、なければ追加
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for (k, v) in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return