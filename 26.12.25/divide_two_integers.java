class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend==Integer.MIN_VALUE && divisor==-1) return Integer.MAX_VALUE;

        boolean negetive= (dividend < 0)^(divisor < 0);


        long a= Math.abs((long)dividend);
        long b= Math.abs((long)divisor);

        int result=0;

        while(a>=b){

            long temp=b, multi=1;

            while(a>=(temp << 1)){
                temp <<= 1; 
                multi <<= 1;
            }
            a-=temp;
            result+= multi;
        }
        return negetive?-result:result;
    }
}
