#2413. Smallest Even Multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        sem = n*2
        for i in range(2*n, n-1, -1):
            if i%n == 0 and i%2 == 0:
                sem = i
        return sem
