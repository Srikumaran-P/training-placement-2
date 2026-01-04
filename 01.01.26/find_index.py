class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i=0
        if needle in haystack:
            while i<len(haystack):
                for m in range(len(needle)):
                    if haystack[m+i] != needle[m]:
                        i=i+1
                        break
                    elif m==len(needle)-1:
                        return i
        else:
            return -1
        
