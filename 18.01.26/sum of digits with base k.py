class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        x=[]
        while n!=0:
            x.append(n%k)
            n=n//k
        return sum(x)

        
