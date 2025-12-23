class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        List<String> ans = new LinkedList<>();
        Map< String , Integer > resturantToIndex = new HashMap<>();
        int minSum = Integer.MAX_VALUE;
        for (int i = 0; i < list1.length; ++i)
        resturantToIndex.put(list1[i],i);
        for (int i = 0; i < list2.length;++i){
            final String resturant = list2[i];
            if (resturantToIndex.containsKey(resturant)){
                final int sum = resturantToIndex.get(resturant) + i;
                if (sum < minSum){
                    minSum = sum;
                    ans.clear();
                    ans.add(resturant);
                } else if (sum == minSum){
                    ans.add(resturant);
                }
            }
        } 
        return ans.toArray(new String[0]); 
    }
}
