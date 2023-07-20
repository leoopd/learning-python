# 2544. Alternating Digit Sum

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = list(str(n))
        switch = False
        sum = 0
        for i in range(len(digits)):
            if switch == False:
                sum += int(digits[i])
                switch = True
            else:
                sum -= int(digits[i])
                switch = False
        return sum
