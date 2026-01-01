class Solution {
    public int majorityElement(int[] nums) {
        //wk that the element will be in majority(x > n/2)
        //boyer moore voting algo

        int candidate = nums[0];
        int count = 1;

        for(int i = 1; i< nums.length;i++){

            if(count == 0){
                //picking a new candidate
                candidate = nums[i];
                count = 1;
            }else if(nums[i]==candidate){
                //if same candidate the count increase
                count++;
            }else{
                //if the element is not same as the candidate
                count--;
            }
        }
        return candidate;
    }
}
