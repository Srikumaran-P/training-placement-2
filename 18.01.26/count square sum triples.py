class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        ct = 0
        for i in range(1,n+1):
            for j in range(1,i+1):
                if i**2 + j**2 == int(math.sqrt(i**2 + j**2))**2 and int(math.sqrt(i**2 + j**2)) <= n:
                    if i != j:
                        ct += 2
                    else:
                        ct += 1
        return ct
