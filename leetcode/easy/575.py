# 575. Distribute Candies

class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        candy_amount = len(set(candyType))
        maximum_eaten = len(candyType)/2
        if maximum_eaten >= candy_amount:
            return candy_amount
        else:
            return maximum_eaten
