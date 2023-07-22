# 2423. Remove Letter To Equalize Frequency

class Solution:
    def equalFrequency(self, word: str) -> bool:
        chars = set(list(word))
        counts = [word.count(x) for x in chars]

        least = counts.index(min(counts))
        if min(counts) == 1:
            option_one = counts[:least] + counts[least+1:]
            print(option_one)
        else:
            option_one = counts.copy()
            option_one[least] -= 1

        if len(option_one) == 1:
            return True

        for i in range(1, len(option_one)):
            if option_one[i-1] != option_one[i]:
                break
            if i == len(option_one)-1:
                return True
        
        most = counts.index(max(counts))
        option_two = counts.copy()
        option_two[most] -= 1

        for i in range(1, len(option_two)):
            if option_two[i-1] != option_two[i]:
                return False
            if i == len(option_two)-1:
                return True
