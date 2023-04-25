# 2129. Capitalize the Title

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        tmp = title.split(' ')
        res = []
        for word in tmp:
            if len(word) <= 2:
                res.append(word.lower())
            else:
                res.append(word.capitalize())
        return ' '.join(res)
