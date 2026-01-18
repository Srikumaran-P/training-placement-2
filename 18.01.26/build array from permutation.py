class Solution(object):
    def buildArray(self, nums):
        a = []
        for i in range(0,len(nums)):
            a.append(nums[nums[i]])
        return a
        
