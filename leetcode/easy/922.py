# 922. Sort Array By Parity II

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        res = []
        for num in nums:
            if num%2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        
        for i in range(len(evens)):
                res.append(evens[i])
                res.append(odds[i])
        
        return res
