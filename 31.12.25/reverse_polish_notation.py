import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for i in tokens:
            if i not in {"+","-","/","*"} :
                stack.append(int(i))
            else:
                a=stack.pop()
                b=stack.pop()
                if i=="+":
                    stack.append(b+a)
                elif i=="-":
                    stack.append(b-a)
                elif i=="*":
                    stack.append(b*a)
                elif i=="/":
                    stack.append(int(float(b)/a))
                else:
                    stack.append(int(i))    
        return stack[0]                               



        
