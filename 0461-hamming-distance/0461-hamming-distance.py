class Solution(object):
    def hammingDistance(self, x, y):
        # XOR を取ると、異なるビットのところだけ1になる
        xor = x ^ y

        # bin()で2進数文字列にして、'1'の数を数えればOK
        return bin(xor).count('1')