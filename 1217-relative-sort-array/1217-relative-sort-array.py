class Solution:
    def relativeSortArray(self, arr1, arr2):
        # arr2の中の各数字に「優先度」を割り振る（小さいほど先に来る）
        priority = {num: i for i, num in enumerate(arr2)}

        # arr1をソート。arr2にないやつは +1000 して最後に回す
        arr1.sort(key=lambda x: priority.get(x, 1000 + x))

        return arr1