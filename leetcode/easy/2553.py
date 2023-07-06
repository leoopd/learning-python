# 2553. Separate the Digits in an Array

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            res.extend(str(num))
        res = [int(x) for x in res]
        return res
