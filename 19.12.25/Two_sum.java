import java.util.ArrayList;
import java.util.Arrays;
class Solution {

public static void main(String[]args){
    Scanner sc= new Scanner(System.in);
    System.out.println("enter the size of array:::::::::");
    int size=sc.nextInt();
    System.out.println("enter the traget:::::::::");
    int target=sc.nextInt();
    int[] arr= new int[size];
    System.out.println("enter the array:::::::::");
    for(int i=0; i<size;i++){
        arr[i]=sc.nextInt();
    }
    System.out.println("final  array is :: "+arr);
    Solution s = new Solution();
    s.twoSum(arr,target);
  }
   public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map= new HashMap<>();

    for(int i=0; i<nums.length;i++){
        int complement=target-nums[i];
        if(map.containsKey(complement)){
            return new int[]{map.get(complement),i};
        }
        map.put(nums[i], i);
    }

    return new int[0];
   }

}

