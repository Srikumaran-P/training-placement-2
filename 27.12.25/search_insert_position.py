class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i=0
        n=len(nums)
        while (i<n and target>nums[i]):
            i+=1
        return i
        
