# 2053. Kth Distinct String in an Array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ctr = 0
        for i in range(len(arr)):
            if arr[i] in arr[arr.index(arr[i])+1:]:
                continue
            ctr += 1
            if ctr == k:
                return arr[i]
        return ""
