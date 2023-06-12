# 283. Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            pass
        else:
            i = 0 
            zeroes = nums.count(0)
            print(zeroes)
            while 0 in nums:
                nums.remove(0)
            for i in range(zeroes):
                nums.append(0)
                i += 1
