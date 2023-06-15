# 771. Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        sum = 0
        for jewel in jewels:
            sum += stones.count(jewel)
        return sum
