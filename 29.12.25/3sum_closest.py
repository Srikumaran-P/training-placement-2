class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            raise ValueError("Need at least 3 numbers")

        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):          # stop at len-3
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # update closest if this sum is nearer to target
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    # exact match
                    return curr_sum

        return closest
