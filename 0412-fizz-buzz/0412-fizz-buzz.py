class Solution(object):
    def fizzBuzz(self, n):

        # 結果を入れていく配列
        answer = []

        # 1からnまで順番に処理していく
        for i in range(1, n + 1):
            # 3と5の両方で割り切れる → "FizzBuzz"
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            # 3で割り切れる → "Fizz"
            elif i % 3 == 0:
                answer.append("Fizz")
            # 5で割り切れる → "Buzz"
            elif i % 5 == 0:
                answer.append("Buzz")
            # どれでもない → 数字を文字列に変換して追加
            else:
                answer.append(str(i))

        # 最終的なリストを返す
        return answer