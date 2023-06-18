# 2215. Find the Difference of Two Arrays

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        return [set(nums1).difference(set(nums2)), set(nums2).difference(set(nums1))]
