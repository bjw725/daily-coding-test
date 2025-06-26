class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0

        total = 0

        for i in range(len(timeSeries) - 1):
            # 次の攻撃までの間隔が duration 未満なら、その間だけ加算
            total += min(duration, timeSeries[i + 1] - timeSeries[i])

        # 最後の攻撃は必ず full duration
        total += duration

        return total