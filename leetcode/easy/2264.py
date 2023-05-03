# 2264. Largest 3-Same-Digit Number in String

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_gint = '-1'
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                if int(num[i]*3) > int(max_gint):
                    max_gint = num[i]*3
        if max_gint == '-1':
            return ''
        return max_gint
