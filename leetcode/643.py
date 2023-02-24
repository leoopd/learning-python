# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = -10001
        for i in range(len(nums)-k+1):
            tmp = 0
            for j in range(i, i+k):
                tmp += nums[j]
            if tmp/k > max_avg:
                max_avg = tmp/k
        return max_avg
