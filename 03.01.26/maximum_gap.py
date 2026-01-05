class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        m=0
        d=0
        if(len(nums)==0):
            return 0
        for i in range(len(nums)-1):
            d=nums[i+1]-nums[i]
            if(d>m):
                m=d
        return m
