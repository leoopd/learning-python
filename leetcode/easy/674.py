674. Longest Continuous Increasing Subsequence

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest_seq = 0
        tmp = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                tmp += 1
            else:
                if tmp > longest_seq:
                    longest_seq = tmp
                    tmp = 1
                else:
                    tmp = 1
        if tmp > longest_seq:
            return tmp
        return longest_seq
