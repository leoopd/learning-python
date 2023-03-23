# 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        sequence = [0, 1, 1]
        for i in range(2, n):
            sequence.append(sequence[i-2]+sequence[i-1]+sequence[i])
        if n == 0:
            return 0
        return sequence[-1]
