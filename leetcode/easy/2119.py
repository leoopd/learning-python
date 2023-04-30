# 2119. A Number After a Double Reversal

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        elif str(num)[-1] == '0':
            return False
        return True
