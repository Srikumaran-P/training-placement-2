class Solution {
    public String longestCommonPrefix(String[] strs) {
        int n = strs.length;

        HashMap<String,Integer> storage = new HashMap<>();
        for(int i=0;i<n;i++){
            String str = strs[i];
            int m = str.length();
            for(int j=1;j<=m;j++){
                String prefix = str.substring(0,j);
                storage.put(prefix,storage.getOrDefault(prefix,0) + 1);
            }
        }

        int len = 0;
        String ans = "";
        for(Map.Entry<String,Integer> set : storage.entrySet()){
            if(set.getValue() == n && set.getKey().length() > len){
                len = set.getKey().length();
                ans = set.getKey();
            }
        }
        return ans;
    }
}
