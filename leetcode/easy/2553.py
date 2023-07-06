# 2553. Separate the Digits in an Array

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            for i in range(len(str(num))):
                res.append(int(str(num)[i]))
        return res
