class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        # ユニークな種類数
        unique_types = len(set(candyType))
        
        # 食べられるキャンディ数（n / 2）
        max_eat = len(candyType) // 2

        # 食べられる最大の種類数を返す
        return min(unique_types, max_eat)