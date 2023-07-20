# 2544. Alternating Digit Sum

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        res = 0
        for i in range(len(n)):
            if i%2 == 0:
                res += int(n[i])
            else:
                res -= int(n[i])
        return res
