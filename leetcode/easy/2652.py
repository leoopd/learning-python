# 2652. Sum Multiples

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        digits = list(range(n+1))
        dsum = 0
        for digit in digits:
            tmp = int(digit)
            if tmp%3 == 0:
                dsum += tmp
            elif tmp%5 == 0:
                dsum += tmp
            elif tmp%7 == 0:
                dsum += tmp
        return dsum
