class Solution {
    public int findLHS(int[] nums) {
     HashMap<Integer,Integer>mp=new HashMap<>();
     for(int i:nums){
        mp.put(i,mp.getOrDefault(i,0)+1);
     }
     List<int []>ll=new ArrayList<>();
     Arrays.sort(nums);
     for(int i=1;i<nums.length;i++){
      if(nums[i]-nums[i-1]==1){
        ll.add(new int[]{nums[i],nums[i-1]});
      }
     }
     int maxi=0;
     for(int i=0;i<ll.size();i++){
        int a[]=ll.get(i);
        int a1=a[0];
        int a2=a[1];
        maxi=Math.max(maxi,mp.get(a1)+mp.get(a2));
     }
     
      return maxi;
    }
}
