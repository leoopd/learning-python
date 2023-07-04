# 1394. Find Lucky Integer in an Array

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ints = [1,2,3,4,5,6,7,8,9]
        counts = {x: arr.count(x) for x in arr}
        for i in range(len(counts)-1, -1, -1):
            if counts.items()[i][0] == counts.items()[i][1]:
                return counts.items()[i][0]
        return -1