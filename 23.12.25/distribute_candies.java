class Solution {
    public int distributeCandies(int[] nums) {
        int x = nums.length;
        Set<Integer> set = new HashSet<>();
        for(int e :nums){
           set.add(e);
        }
        return Math.min(x/2,set.size());

    }
}
