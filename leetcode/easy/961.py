# 961. N-Repeated Element in Size 2N Array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        occurred = {}
        for num in nums:
            try:
                if occurred[num]:
                    return num
            except:
                occurred[num] = True
