# 1304. Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 2:
            return [1, -1]
        res_sum = 0
        res = []
        for i in range(n-1):
            res.append(i)
            res_sum += i
        res.append(-res_sum)
        return res
