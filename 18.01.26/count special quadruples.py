class Solution(object):
    def countQuadruplets(self, nums):
        value = 0
        for a,b,c,d in combinations(nums, 4):
            if a+b+c == d:
                value += 1
        return value
        
        # Combinations is used to generate all possible combinations of a specified length
