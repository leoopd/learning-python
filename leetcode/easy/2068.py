# 2068. Check Whether Two Strings are Almost Equivalent

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        chars = set(list(word1+word2))
        occs = []
        
        for char in chars:
            occs.append(word1.count(char))
            occs.append(word2.count(char))

        for i in range(1, len(occs), 2):
            if occs[i-1] < occs[i]-3 or occs[i-1] > occs[i]+3:
                return False
        
        return True
