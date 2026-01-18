class Solution(object):
    def getLucky(self, s, k):
        value =[]
        for ch in s:
            m= ord(ch.lower()) - ord('a')+1
            value.append(str(m))
        new_list = ''.join(value)

        for _ in range(k):
            digits = [int(x) for x in new_list]    
            total = sum(digits)
            new_list = str(total)
        new_list = int(new_list)    
        return new_list    

          
        
