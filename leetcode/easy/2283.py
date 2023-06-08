# 2283. Check if Number Has Equal Digit Count and Digit Value

class Solution(object):
    def digitCount(self, num):
        num_list = list(num)
        for i in range(len(num)):
            if str(num_list.count(str(i))) != num[i]:
                return False
        return True
