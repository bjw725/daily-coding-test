class Solution:
    def sortSentence(self, s):
        # 空白で単語に分割
        words = s.split()

        # 各単語を (位置, 本体) に変換してソート
        # 単語の最後の文字が位置番号なので、[:-1] で本体, [-1] で位置を取り出す
        words_sorted = sorted(words, key=lambda w: int(w[-1]))

        # 数字を削除した単語だけを取り出して結合
        return ' '.join(w[:-1] for w in words_sorted)