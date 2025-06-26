class Solution:
    def isHappy(self, n):
        def get_next(number):
            total = 0
            while number > 0:
                digit = number % 10
                total += digit * digit
                number //= 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1