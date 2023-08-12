# 1437. Check If All 1's Are at Least Length K Places Away

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        try:
            start = nums.index(1)
        except:
            return True

        for i in range(start, len(nums)):
            if nums[i] == 1:
                try:
                    tmp = nums[i+1:i+k+1]
                except:
                    tmp = nums[i+1:]
                if 1 in tmp:
                    return False
        return True
