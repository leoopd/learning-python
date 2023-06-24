# 1624. Largest Substring Between Two Equal Characters

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        max_length = -1
        for letter in string.ascii_lowercase:
            if s.count(letter) > 1:
                left = s.index(letter)
                right = s.rindex(letter)
                length = len(s[left+1:right])
                if length > max_length:
                    max_length = length
        return max_length
