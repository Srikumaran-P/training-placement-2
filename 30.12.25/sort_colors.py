class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        mx = max(nums)
        n = len(nums)
        freq = [0]*(mx+1)
        for i in nums:
            freq[i] += 1

        nums[:] = []
        for i in range(mx + 1):
            while freq[i]>0:
                nums.append(i)
                freq[i] -= 1    
        
