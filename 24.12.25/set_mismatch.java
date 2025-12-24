class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int s=0,grt;
        for(int i=0;i<k;i++)
        s=s+nums[i];
        grt=s;
        for(int i=k;i<nums.length;i++)
        {
            s=s+nums[i];
            s=s-nums[i-k];
            grt=Math.max(s,grt);
        }
        double avg=grt;
        return avg/k;
    }
}
