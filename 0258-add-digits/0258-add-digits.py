class Solution(object):
    def addDigits(self, num):

        # 0の場合はそのまま0を返す
        if num == 0:
            return 0

        # 9で割った余りが答えになる（例外として、余り0のときは9を返す）
        return 9 if num % 9 == 0 else num % 9