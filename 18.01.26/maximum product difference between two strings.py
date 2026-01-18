class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        n = len(s) - 1
        return (s[n] * s[n-1]) - (s[0] * s[1])
