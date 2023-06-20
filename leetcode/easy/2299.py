# 2299. Strong Password Checker II

class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        check_list = [0, 0, 0, 0]
        special_chars = '!@#$%^&*()-+'
        import string

        if len(password) < 8:
            print('2')
            return False

        for i in range(len(password)):
            if i < len(password)-1 and password[i] == password[i+1]:
                return False
            if password[i] in string.ascii_lowercase:
                check_list[0] = 1            
            if password[i] in string.ascii_uppercase:
                check_list[1] = 1
            if password[i] in string.digits:
                check_list[2] = 1       
            if password[i] in special_chars:
                check_list[3] = 1

        print(check_list)
        for element in check_list:
            if element == 0:
                return False
        return True
