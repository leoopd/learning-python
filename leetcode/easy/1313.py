# 1313. Decompress Run-Length Encoded List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(1, len(nums), 2):
            tmp = nums[i-1]*str(nums[i])
            tmp2 = [nums[i] for x in range(nums[i-1])]
            result += tmp2
        return result
