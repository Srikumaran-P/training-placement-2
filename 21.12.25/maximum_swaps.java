class Solution {
    public int maximumSwap(int num) {

        char[] nums = Integer.toString(num).toCharArray();
        int n = nums.length;

        int[] maxInd = new int[n];
        maxInd[n - 1] = n - 1;

        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] > nums[maxInd[i + 1]]) {
                maxInd[i] = i;
            } else {
                maxInd[i] = maxInd[i + 1];
            }
        }

       
        for (int i = 0; i < n; i++) {
            int best = maxInd[i];
            if (nums[i] < nums[best]) {
                // swap
                char temp = nums[i];
                nums[i] = nums[best];
                nums[best] = temp;
                break;      
            }
        }

        return Integer.parseInt(new String(nums));
    }
}
