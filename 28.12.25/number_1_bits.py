class Solution(object):
    def hammingWeight(self, n):
        val = format(n,"b")
        val = val.count("1")
        return val
