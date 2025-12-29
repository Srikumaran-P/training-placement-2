class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a=len(nums1)+len(nums2)
        b=nums1+nums2
        b.sort()
        c=a/2
        if a%2==0:
            return ((b[c]+b[c-1])/2.0)
        else:
            return b[c]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
