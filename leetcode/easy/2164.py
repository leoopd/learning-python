# 2164. Sort Even and Odd Indices Independently

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in range(nums):
            if i%2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        evens.sort()
        odds[::-1].sort()
        for i in range(0, len(odds), 2):
            if i < len(odds):
                nums[i] = o
