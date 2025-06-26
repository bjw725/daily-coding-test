class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Alice wins if n is even, loses if n is odd
        return n % 2 == 0