# 2544. Alternating Digit Sum

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = list(str(n))
        sum = 0
        for i in range(len(digits)):
            if i%2 == 0:
                sum += int(digits[i])
            else:
                sum -= int(digits[i])
        return sum
