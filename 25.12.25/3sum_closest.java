class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int sum = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.length; i++) {
            int l = i + 1;
            int r = nums.length - 1;
            while (l < r) {
                int currentSum = nums[i] + nums[l] + nums[r];
                if (currentSum > target) {
                    r--;
                }else if(currentSum < target){
                    l++;
                }else{
                    return currentSum;
                }
                sum = Math.abs(currentSum - target) < Math.abs(sum - target) ? currentSum : sum;
            }
        }
        return sum;
    }
}
