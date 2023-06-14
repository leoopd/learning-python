# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution(object):
    def subtractProductAndSum(self, n):
        digit_product = n%10
        digit_sum = digit_product
        n = n/10
        while n > 0:
            tmp = n%10
            n = n/10
            digit_product *= tmp
            digit_sum += tmp
        return digit_product - digit_sum
