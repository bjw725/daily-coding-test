from collections import Counter

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 最初の単語の文字カウントで初期化
        common = Counter(words[0])

        # 残りの単語と共通部分を取り続ける
        for word in words[1:]:
            common &= Counter(word)

        # Counterをリスト化（文字を出現回数だけ展開）
        result = []
        for char, freq in common.items():
            result.extend([char] * freq)

        return result