class Solution {
    public static void nextPermutation(int[] nums) {
            for(int i = nums.length - 1; i >= 1; i--) {
                if (nums[i] <= nums[i-1])
                    continue;
                else {
                    int idx = upperBound(nums, i, nums[i-1]);
                    swap(nums, i-1, idx);
                    reverse(nums, i);
                    return;
                }
            }
            reverse(nums, 0);
    }

    static void reverse (int nums[], int left) {
        // two pointer approach
        int i = left;
        int j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    static void swap (int nums[], int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] =  temp;
    }


    // find the index of element in the given portion that its value > target (binary search-based )
    static int upperBound(int[]nums, int left, int target) {
        int right = nums.length - 1;
        int answer =  -1; // indicate not found as a fallback (actually cannot happen because this method is called only when exist at least one element in that portion of array > target)
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] > target) {
                answer = mid; // candidate
                left = mid + 1; // try to find smaller > target
            }
            else {
                right = mid - 1;
            }
        }
        return answer;
    }
}
