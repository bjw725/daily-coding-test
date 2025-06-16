class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # スコアを降順にソートし、順位付け
        sorted_scores = sorted(score, reverse=True)

        # スコアから順位ラベルへの辞書を作成
        rank_map = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)

        # 元のスコア順にラベルを並べる
        return [rank_map[s] for s in score]