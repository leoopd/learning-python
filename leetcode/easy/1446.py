# 1446. Consecutive Characters

class Solution:
    def maxPower(self, s: str) -> int:
        max = 0
        ctr = 1
        if len(s) == 1:
            return 1
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                ctr += 1
            else:
                if ctr > max:
                    max = ctr
                ctr = 1
        if ctr > max:
            max = ctr
        return max
