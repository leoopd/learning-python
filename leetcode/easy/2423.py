# 2423. Remove Letter To Equalize Frequency

class Solution:
    def equalFrequency(self, word: str) -> bool:
        switch = False
        chars = set(list(word))
        counts = [word.count(x) for x in chars]
        if counts[0] <= counts[-1]:
            occ = counts[0]
        else:
            occ = counts[-1]
        counts[counts.index(counts.max())] -= 1
        print(counts)
        for i in range(len(counts)):
            if counts[i] == occ+1 and switch == False:
                switch = True
            elif counts[i] > occ:
                return False
        return True
