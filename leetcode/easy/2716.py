# 2716. Minimize String Length

class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(set(s))
