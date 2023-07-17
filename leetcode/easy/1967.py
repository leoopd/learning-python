# 1967. Number of Strings That Appear as Substrings in Word

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ctr = 0
        for pattern in patterns:
            if pattern in word:
                ctr += 1
        return ctr
