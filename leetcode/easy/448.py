448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = list(range(1, len(nums)+1))
        for num in nums:
            if num in res:
                res.remove(num)
        return res
