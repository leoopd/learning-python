# 2006. Count Number of Pairs With Absolute Difference K

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] - nums[j] == k or (nums[i] - nums[j])*-1 == k:
                    count += 1
        return count
