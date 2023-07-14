# 2506. Count Pairs Of Similar Strings

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ctr = 0
        for i in range(len(words)):
            tmp = set(list(words[i]))
            for j in range(i+1, len(words)):
                if tmp == set(list(words[j])):
                    ctr += 1
        return ctr
