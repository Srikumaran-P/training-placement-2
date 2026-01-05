
class Solution(object):
    def lengthOfLastWord(self, s):
       
        n = len(s.split())
        return len(s.split()[n-1])

        
        
