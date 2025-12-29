class Solution:
    def divide(self, dividend, divisor) :
        int_max= 2**31-1
        int_min= -2**31

        if dividend==int_min and divisor==-1:
            return int_max
        if divisor==1:
            return dividend
        elif divisor==-1:
            return -dividend
        else:
            sign=1 if(dividend>0)==(divisor>0)else-1
            dividend=abs(dividend)
            divisor=abs(divisor)
            qoutient=0
            while dividend>=divisor:
                temp_divisor,multiple=divisor,1
                while dividend>=(temp_divisor<<1):
                    temp_divisor<<=1
                    multiple<<=1
                dividend-=temp_divisor
                qoutient+=multiple
            qoutient*=sign
            if qoutient>int_max:
                return int_max
            elif qoutient<int_min:
                return int_min
            else:
                return qoutient
