# 2042. Check if Numbers Are Ascending in a Sentence

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        string_list = s.split(" ")
        last_int = 0
        for string in string_list:
            if string.isdigit():
                if int(string) <= last_int:
                    return False
                last_int = int(string)
        return True
