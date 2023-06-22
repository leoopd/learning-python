# 942. DI String Match

class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ints = list(range(len(s)+1))
        perm = []
        for digit in s:
            if digit == 'I':
                perm.append(ints.pop(0))
            else:
                perm.append(ints.pop(-1))
        perm.append(ints.pop(0))
        return perm
