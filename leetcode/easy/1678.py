# 1678. Goal Parser Interpretation

class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        res = ""
        while i < len(command):
            if i < len(command)-3 and command[i:i+4] == "(al)":
                res += "al"
                i += 4
            elif i < len(command)-1 and command[i:i+2] == "()":
                res += "o"
                i += 2
            elif command[i] == "G":
                res += "G"
                i += 1
        return res
