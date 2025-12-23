class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> res=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=-1){
                int j=nums[i]-1;
                while(j>=0 && nums[j]!=-1){
                    int temp=nums[j];
                    nums[j]=-1;
                    j=temp-1;
                }
            }
        }
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=-1){
                res.add(i+1);
            }
        }
        return res;
    }
}
