class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int n = nums.length;
        if(n==0 || n == 1) return n;
        int count = 1;
        int result = 0;
        for(int i =0;i<nums.length - 1;i++){
            if(nums[i] < nums[i+1]){
                count++;
            }else{
                count = 1;
            }

            if(result < count){
                result = count;
            }
        }
        return result;
    }
}
