# 2351. First Letter to Appear Twice

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = {}
        for i in range(len(s)):
            try:
                letters[s[i]] += 1
            except:
                letters[s[i]] = 1
            if letters[s[i]] == 2:
                return s[i]
