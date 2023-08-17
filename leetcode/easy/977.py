# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [x*x for x in nums]
        res.sort()
        return res
