class Solution {
    public static int fact(int num){
        int sum=0;
        for(int i=1;i<num;i++){
            if(num % i==0){
                sum=sum+i;
            }
        }
        return sum;
    }
    public boolean checkPerfectNumber(int num) {
        int sum=fact(num);
        return (sum==num);
    }
}
