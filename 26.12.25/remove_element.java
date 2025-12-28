class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length <= 0) {
            return 0;
        }
        // swap val to end to avoid create new int array
        int j = nums.length - 1;
        int i = 0;
        while(i <= j) {
            int val_in_i = nums[i];
            // if equals, should swap with j
            if(val_in_i == val) {
                int tmp = nums[j];
                nums[j] = val_in_i;
                nums[i] = tmp;
                j -= 1;
            } else {
                // forward if not equals 
                i += 1;
            }
        }
        return j + 1;
    }
}
