# 1920. Build Array from Permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for digit in nums:
            ans.append(nums[digit])
        return ans
