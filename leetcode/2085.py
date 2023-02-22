# 2085. Count Common Words With One Occurrence

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ctr = 0
        for word in words1:
            if words1.count(word) == 1 and words2.count(word) == 1:
                ctr += 1
        return ctr
