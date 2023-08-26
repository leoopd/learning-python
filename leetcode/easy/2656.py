# 2656. Maximum Sum With Exactly K Elements

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        digit = max(nums)
        res = digit
        while k > 1:
            digit += 1
            res += digit
            k -= 1
        return res
