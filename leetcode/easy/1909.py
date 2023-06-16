# 1909. Remove One Element to Make the Array Strictly Increasing

class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                if i == len(nums)-1:
                    return True
                elif nums[i-1] < nums[i+1]:
                    del nums[i]
                    break
                elif nums[i] < nums[i+1]:
                    del nums[i-1]
                    break
                else:
                    return False
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
        return True
