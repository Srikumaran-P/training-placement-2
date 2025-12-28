class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length();
        int k  = needle.length();

        for(int i = 0;i<=n-k;i++){
            String subString = haystack.substring(i,i+k); //create the substring 
            if(subString.equals(needle))return i; //compare retuen the result
        }

        return -1;
    }
}
