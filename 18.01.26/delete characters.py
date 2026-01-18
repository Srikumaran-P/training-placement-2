class Solution(object):
    def makeFancyString(self,s):

        stack=[]
        for i in range(len(s)):

            stack.append(s[i]) 
            
            while len(stack) >= 3 and stack[-1]==stack[-2]==stack[-3]:
                stack.pop()

        
        k=""
        for i in stack:
            k=k+i
        return k
