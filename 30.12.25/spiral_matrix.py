class Solution(object):
    def generateMatrix(self, n):
        c=1
        t=0
        b=n-1
        l=0
        r=n-1
        matrix=[[ 0 for i in range(n)] for _ in range(n)]
        while t<=b and l<=r:
            for i in range(l,r+1):
                matrix[t][i]=c
                c+=1
            
            t+=1
            for i in range(t,b+1):
                matrix[i][r]=c
                c+=1
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    matrix[b][i]=c
                    c+=1
            b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    matrix[i][l]=c
                    c+=1
            l+=1
        return matrix

        
