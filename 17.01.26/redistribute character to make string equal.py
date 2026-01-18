class Solution(object):
    def makeEqual(self, words):
        a="".join(words)
        b=list(set(a))
        for x in b:
            if a.count(x)%len(words)!=0:
                return False
        return True
        
