class Solution(object):
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()                    # Step 1: Sort
        result = []
        n = len(nums)
        
        for i in range(n - 2):         # i up to n-3
            if i > 0 and nums[i] == nums[i-1]:   # Skip duplicate i
                continue
            
            target = -nums[i]          # We need left + right = target
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result
