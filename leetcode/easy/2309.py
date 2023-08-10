# 2309. Greatest English Letter in Upper and Lower Case

class Solution:
    def greatestLetter(self, s: str) -> str:
        lower = {}
        upper = {}
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for digit in s:
            if digit.islower():
                lower[digit.upper()] = True
            else:
                upper[digit] = True
        
        for char in alph[::-1]:
            try:
                if lower[char] and upper[char]:
                    return char
            except:
                continue
        return ""
