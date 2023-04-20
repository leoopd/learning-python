# 2042. Check if Numbers Are Ascending in a Sentence

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        string_list = s.split()
        int_list = []
        ints = '0123456789'
        for e in string_list:
            if e[0] in ints:
                int_list.append(int(e))
        print(int_list)
        for i in range(1, len(int_list)):
            if int_list[i-1] >= int_list[i]:
                return False
        return True
