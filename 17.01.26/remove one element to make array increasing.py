class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        if len(nums) < 3:
            return True
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]:
                count += 1
                if count > 1:
                    return False
            if i-2 >= 0 and nums[i-2] >= nums[i]:
                nums[i] = nums[i-1]
        return True
