class Solution(object):
    def climbStairs(self, n):
        c = 1
        a,b = 0,1
        for i in range(n):
            c+=a
            a,b = b,a+b
        return c


        
        
