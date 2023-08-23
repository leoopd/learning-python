# 1408. String Matching in an Array

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            tmp = words[:i] + words[i+1:]
            for j in range(len(tmp)):
                if words[i] in tmp[j]:
                    res.append(words[i])
                    break
        return res
