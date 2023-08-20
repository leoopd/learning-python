# 500. Keyboard Row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiopQWERTYUIOP"
        second_row = "asdfghjklASDFGHJKL"
        third_row = "zxcvbnmZXCVBNM"
        one = True
        two = True
        three = True
        res = []
        for word in words:
            for letter in word:
                if letter not in first_row:
                    one = False
                if letter not in second_row:
                    two = False
                if letter not in third_row:
                    three = False
            if one or two or three:
                res.append(word)
            one = True
            two = True
            three = True
            
        return res
