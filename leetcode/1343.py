# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ctr = 0
        for i in range(len(arr)-k+1):
            tmp = 0
            for j in range(i, i+k):
                tmp += arr[j]
            if tmp/k >= threshold:
                ctr += 1
        return ctr
