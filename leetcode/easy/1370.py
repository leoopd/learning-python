# 1370. Increasing Decreasing String

class Solution:
    def sortString(self, s: str) -> str:
        characters = list(s)
        res = ""
        while len(characters) > 0:
            tmp = list(set(characters))
            tmp.sort()
            for char in tmp:
                res += char
                characters.remove(char)
            if len(characters) == 0:
                break
            tmp = list(set(characters))
            tmp.sort()
            for char in list(tmp)[::-1]:
                res += char
                characters.remove(char)
        return res
