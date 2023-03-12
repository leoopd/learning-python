# 1750. Minimum Length of String After Deleting Similar Ends

class Solution:
    def minimumLength(self, s: str) -> int:
        '''This function return the minimum Length of the given string, after deleting matching pre- and suffixes.
        For more details, reference leetcode.com'''

        # Cond 1: len(s) > 0
        # Cond 2: prefix == suffix
        # Cond 3: no intersecting indexes

        while len(s) > 0:                                       # Cond 1
            if s[0] != s[-1]:                                   # Cond 2
                break
            left_idx, right_idx = 0, len(s)-1
            for i, left_char in enumerate(s):
                if i == len(s)-1:                               # Cond 3
                    return 0
                if left_char != s[0]:                           # If Cond 2 fails
                    left_idx = i
                    break
            for j, right_char in reversed(list(enumerate(s))):  # enumerates s in reverse
                if right_char != s[-1]:                         # If Cond 2 fails
                    right_idx = j+1
                    break
            s = s[left_idx:right_idx]                           # Deletes the pre- and suffix
        return len(s)
