class Solution(object):
    def reverseWords(self, s):
        # スペースで単語を分ける
        words = s.split()

        # 各単語を1つずつ反転させる
        reversed_words = [word[::-1] for word in words]

        # 再びスペースで結合して1つの文に戻す
        return ' '.join(reversed_words)