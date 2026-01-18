class Solution(object):
    def countGoodSubstrings(self, s):
        a=0
        for i in range(len(s)-2):
            x=s[i:i+3]
            n=True
            for i in x:
                if x.count(i)>1:
                    n=False
                    break
            if n:
                a+=1
        return a
            


        
