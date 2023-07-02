# 1704. Determine if String Halves Are Alike

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = 0
        for vowel in vowels:
            left += s[:len(s)/2].count(vowel)
            right += s[len(s)/2:].count(vowel)
        if left == right:
            return True
        return False
