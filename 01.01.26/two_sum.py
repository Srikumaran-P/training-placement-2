class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        b = 1
        while True:
            ans = nums[i] + nums[b]
            if ans == target:
                return [i, b]
            elif b != len(nums)-1:
                b += 1
            else:
                i += 1
                b = i + 1
            
