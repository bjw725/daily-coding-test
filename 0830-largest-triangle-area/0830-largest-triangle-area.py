import itertools

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p1, p2, p3):
            # 三角形の面積 = |(x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)) / 2|
            return abs(
                p1[0]*(p2[1] - p3[1]) +
                p2[0]*(p3[1] - p1[1]) +
                p3[0]*(p1[1] - p2[1])
            ) / 2.0

        max_area = 0
        for p1, p2, p3 in itertools.combinations(points, 3):
            max_area = max(max_area, area(p1, p2, p3))

        return max_area