# 2053. Kth Distinct String in an Array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ctr = 0
        for string in arr:
            if arr.count(string) == 1:
                ctr += 1
            if ctr == k:
                return string
        return ""
