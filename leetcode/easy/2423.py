# 2423. Remove Letter To Equalize Frequency

class Solution:
    def equalFrequency(self, word: str) -> bool:
        chars = set(list(word))
        counts = {x: word.count(x) for x in chars}
        
        #Sorting the dict by occurrences
        sorted_counts = dict(sorted(counts.items(), key=lambda x:x[1]))
        values = list(sorted_counts.values())
        
        #Removing one instance of the most occurring letter
        tmp = values.copy()
        tmp[-1] -= 1
        for i in range(1, len(tmp)):
            if tmp[i-1] != tmp[i]:
                break
            if i == len(tmp)-1:
                return True

        #Removing one instance of the least occurring letter
        tmp = values.copy()
        tmp[0] -= 1
        for i in range(1, len(tmp)):
            if tmp[i-1] == 0:
                continue
            if tmp[i-1] != tmp[i]:
                return False

        return True
