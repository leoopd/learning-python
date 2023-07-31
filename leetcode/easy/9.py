# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digit_list = list(str(x))
        j = len(digit_list)-1

        if len(digit_list)%2 == 0:
            switch = False
        else:
            switch = True
            breaker = len(digit_list)/2-1

        for i in range(len(digit_list)):
            if digit_list[i] != digit_list[j]:
                return False
            j -= 1
            if switch and i == breaker:
                break
                
        return True
