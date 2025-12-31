class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        j = 1

        count = 0

        while j < len(nums):
            
            if nums[j] == nums[j-1] and count<1:
                nums[i] = nums[j]
                count += 1
                
                i += 1
                j += 1
            elif nums[j] == nums[j-1] and count >=1:
                count += 1
                j += 1
            else:
                count = 0
                nums[i] = nums[j]
                i += 1
                j += 1
        return i
