# 482. License Key Formatting

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = ''.join(s.split('-'))
        amt = k
        res = ''
        for i in range(len(chars)-1, -1, -1):
            res += chars[i].upper()
            amt -= 1
            if i == 0:
                return res[::-1]
            if amt == 0:
                res += '-'
                amt = k
                
        return ""
