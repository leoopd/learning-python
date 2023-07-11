#645. Set Mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        original = list(range(1, len(nums)+1))
        res = [0, 0]
        for i in range(len(nums)):
            if original[i] not in nums:
                res[1] =  original[i]
            elif nums.count(nums[i]) == 2:
                res[0] = nums[i]
                nums[i] = 0
        
            if res[0] != 0 and res[1] != 0:
                return res
