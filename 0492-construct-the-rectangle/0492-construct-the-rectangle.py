import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # 幅Wを√area から1まで試し、最初に割り切れたところで長さLを求める
        for W in range(int(math.sqrt(area)), 0, -1):
            if area % W == 0:
                L = area // W
                return [L, W]