def maxSubArray(nums):
    cur = res = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        res = max(res, cur)
    return res
