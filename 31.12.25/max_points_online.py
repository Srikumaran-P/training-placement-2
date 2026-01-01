class Solution(object):
    def maxPoints(self, points):
        if len(points)==1 :
            return(1)
        maxslope=2
        for i in range (len(points)-1) :
            for j in range(i+1,len(points)-1) :
                currentslope=2
                for k in range(j+1,len(points)) :
                    if (    (  (points[j][1]-points[i][1])*(points[k][0]-points[i][0])  ) == (  (points[k][1]-points[i][1])*(points[j][0]-points[i][0])  )  ) :
                        currentslope=currentslope+1
                maxslope=max(currentslope,maxslope)

        return(maxslope)
    
        
