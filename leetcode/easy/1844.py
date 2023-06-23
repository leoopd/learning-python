# 1844. Replace All Digits with Characters

class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''
        for i in range(1, len(s), 2):
            ascii = ord(s[i-1])
            ascii += int(s[i])
            res += s[i-1] + chr(ascii)
        if len(s)%2 == 0:
            return res
        return res + s[-1]
