class Solution(object):
    def maxArea(self, height):
        p1 = 0
        p2 = len(height)-1
        area = 0
        largest = 0
        while p1 < p2:
            if height[p1]<=height[p2]:
                area = (height[p1])*(p2-p1)
                p1 += 1
            elif height[p1]>height[p2]:
                area = (height[p2])*(p2-p1)
                p2 -= 1
            largest = max(largest,area)
        return largest




        
