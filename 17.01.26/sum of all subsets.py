class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: O(n)
        Space: O(1)

        Solution Explanation:
        1. For any set of n elements, there exist 2^n subsets.
        2. The value at digit x << b, of XORing n elements, will equal 1 exactly when an odd number of those n elements hold a 1 at position x << b. Else equals 0.
        3. Thus, for any "on" bit for some elem x in elems:
            - We either contain / don't contain that x for each of the 2^(n - 1) subsets excluding it. 
            - Instead of counting every subset, we can equivalently OR all n elements to determine every bit that is ever "on."
                - Then, simply multiply by 2^(n - 1), which is equivalent to the (intuitive) partial product.
        4. Return
        """
        # 1. Instantiate and build Global OR
        global_or = 0
        for num in nums:  # O(n)
            global_or |= num
        # 2. Return Statement - justified by combinatorics
        return global_or * 2 ** (len(nums) - 1)  # O(1)
        
