# 2357. Make Array Zero by Subtracting Equal Amounts

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        rsum = 0
        biggest = nums[-1]
        if sum(nums) == 0:
            return 0
        for num in nums:
            tmp = num - rsum
            if tmp <= 0:
                continue
            biggest -= tmp
            rsum += tmp
            if biggest <= 0:
                return count
            else:
                count += 1
        return count
