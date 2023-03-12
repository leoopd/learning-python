# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        res = ''
        for i in range(len(s)-1, -1, -1):
            if s[i] in 'aeiouAEIOU':
                vowels.append(s[i])
        for char in s:
            if char in 'aeiouAEIOU':
                res += vowels[0]
                vowels = vowels[1:]
                continue
            res += char
        return res
