# 500. Keyboard Row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        one = True
        two = True
        three = True
        res = []
        for word in words:
            tmp = word.lower()
            for letter in tmp:
                if one and letter not in first_row:
                    one = False
                if two and letter not in second_row:
                    two = False
                if three and letter not in third_row:
                    three = False
                if not one and not two and not three:
                    break
            if one or two or three:
                res.append(word)
            one = True
            two = True
            three = True
            
        return res
