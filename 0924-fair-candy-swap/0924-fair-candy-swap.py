class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumB - sumA) // 2  # y - x = (sumB - sumA) / 2
        
        setB = set(bobSizes)  # 検索高速化
        
        for x in aliceSizes:
            if x + diff in setB:
                return [x, x + diff]