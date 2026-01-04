class Solution(object):
    def plusOne(self, digits):
        stri=int(''.join(map(str,digits)))+1
        digit_list = [int(digit) for digit in str(stri)]   
        return digit_list
        
