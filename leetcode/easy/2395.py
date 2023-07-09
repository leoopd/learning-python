# 2395. Find Subarrays With Equal Sum

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        res = dict()
        for i in range(1, len(nums)):
            try:
                if res[nums[i-1]+nums[i]]:
                    return True
            except:
                res[nums[i-1]+nums[i]] = True
        return False
