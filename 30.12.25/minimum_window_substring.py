class Solution(object):
    def check(self,formed, required):
        if formed == required:
            return True 
        else:
            return False
            
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        low = 0 
        res = 999999999
        end = 0 
        start = 0 
        length = 0
        s_lst = [0] * 256
        t_lst = [0]*256
        formed = 0 
        ans = 0
        for i in t:
            if t_lst[ord(i)] >= 1:
                ans+=1
            t_lst[ord(i)] += 1
        required = len(t) - ans
        for high in range(n):
            s_lst[ord(s[high])] += 1
            if s_lst[ord(s[high])] == t_lst[ord(s[high])]:
                formed+=1
            while self.check(formed, required):
                length = (high-low) + 1
                if length < res:
                    res = length 
                    start = low
                    end = high+1
                s_lst[ord(s[low])] -= 1
                if s_lst[ord(s[low])] < t_lst[ord(s[low])]:
                    formed-=1
                low+=1
        return (s[start:end])
