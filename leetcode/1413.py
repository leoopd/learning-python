# 1413. Minimum Value to Get Positive Step by Step Sum

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1
        running = 1
        for element in nums:
            running += element
            if running < 1:
                start += (running*-1)+1
                running = 1
        return start
