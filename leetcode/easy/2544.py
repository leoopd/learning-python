# 2544. Alternating Digit Sum

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        switch = False
        n = str(n)
        res = 0
        for digit in n:
            if switch:
                res -= int(digit)
                switch = False
            else:
                res += int(digit)
                switch = True
        return res
