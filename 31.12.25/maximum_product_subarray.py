class Solution {

    public int maxProduct(int[] nums) {

        int res = nums[0];

        int minProd = nums[0];

        int maxProd = nums[0];

        for(int i = 1; i < nums.length; i ++)
        {

            int num = nums[i];

            int tempMin = Math.min(num, Math.min(num * minProd, num * maxProd));

            int tempMax = Math.max(num, Math.max(num * minProd, num * maxProd));

            minProd = tempMin;

            maxProd = tempMax;

            res = Math.max(res, maxProd);
        }

        return res;
    }
}
