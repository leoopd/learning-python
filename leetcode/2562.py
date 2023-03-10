# 2562. Find the Array Concatenation Value

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat_value = 0
        while len(nums) > 1:
            tmp = str(nums[0]) + str(nums[-1])
            nums = nums[1:-1]
            concat_value += int(tmp)
        if len(nums) == 1:
            concat_value += nums[0]
        return concat_value
