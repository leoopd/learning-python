# 905. Sort Array By Parity

class Solution(object):
    def sortArrayByParity(self, nums):
        num1, num2 = [], []
        for num in nums:
            if num%2 == 0:
                num2.append(num)
            else:
                num1.append(num)
        return num2 + num1
