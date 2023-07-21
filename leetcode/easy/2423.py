# 2423. Remove Letter To Equalize Frequency

class Solution:
    def equalFrequency(self, word: str) -> bool:
        chars = set(list(word))
        counts = [word.count(x) for x in chars]
        biggest = max(counts)
        if biggest != 1:
            counts[counts.index(biggest)] -= 1

        for i in range(1, len(counts)):
            if counts[i] != counts[i-1]:
                return False
        return True
