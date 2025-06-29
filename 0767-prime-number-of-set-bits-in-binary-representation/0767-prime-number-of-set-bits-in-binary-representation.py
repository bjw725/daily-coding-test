class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # 32ビットまでの数値なので、1〜32のうちの素数をあらかじめ定義
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        count = 0

        for num in range(left, right + 1):
            # bin(num) は '0b10101' のようになるので、1の数をカウント
            set_bits = bin(num).count('1')
            if set_bits in primes:
                count += 1

        return count