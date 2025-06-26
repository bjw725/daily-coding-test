import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Pythonのheapqはmin-heapなので、すべてを負の値にしてmax-heapとして扱う
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)  # 最大
            second = -heapq.heappop(stones) # 2番目に大きい
            if first != second:
                heapq.heappush(stones, -(first - second))

        return -stones[0] if stones else 0