# 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        ctr = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                ctr += 1
        return ctr
