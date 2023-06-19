# 409. Longest Palindrome

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        switch = False
        letters = {l: s.count(l) for l in set(s)}
        for letter in letters:
            if letters[letter]%2 == 0:
                res += letters[letter]
            else:
                switch = True
                res += letters[letter]-1
        if switch == True:
            return res + 1
        else:
            return res
