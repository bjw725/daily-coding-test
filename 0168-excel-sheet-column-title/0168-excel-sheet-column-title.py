class Solution:
    def convertToTitle(self, columnNumber):
        result = ''
        while columnNumber > 0:
            columnNumber -= 1  # A:1 → Z:26 → AA:27の調整
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result