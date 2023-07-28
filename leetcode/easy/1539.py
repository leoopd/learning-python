# 1539. Kth Missing Positive Number

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ctr = 0
        i = 0
        while True:
            i += 1
            if i not in arr:
                ctr += 1
            if ctr == k:
                return i
