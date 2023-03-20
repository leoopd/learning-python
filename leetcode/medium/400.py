class Solution:
    def findNthDigit(self, n: int) -> int:
        res = ''
        for i in range(1, n+1):
            res += str(i)
            if len(res) == n:
                break
        return int(res[n-1])
