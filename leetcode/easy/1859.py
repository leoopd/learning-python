# 1859. Sorting the Sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split(" ")
        tmp_list = [None] * len(s_list)
        print(tmp_list)
        for word in s_list:
            tmp_list[int(word[-1])-1] = word[:-1]       
        return " ".join(tmp_list)
