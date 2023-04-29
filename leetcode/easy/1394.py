# 1394. Find Lucky Integer in an Array

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ctr = 1
        arr.sort()
        while len(arr) > 0:
            num = arr.pop(-1)
            while num in arr:
                arr.remove(num)
                ctr += 1
            if num == ctr:
                return num
            else:
                ctr = 1
        return -1
