# 1539. Kth Missing Positive Number

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ints = 1
        while k > 0:
            if k == 1 and ints not in arr:
                return ints
            if ints not in arr:
                ints += 1
                k -= 1
            else:
                ints += 1
        return ints
