class Solution {
    public int lengthOfLongestSubstring(String s) {

        HashMap<Character, Integer> m = new HashMap<>();
        int max = 0;
        int i =0;
         int j =0;

         while(j<s.length()){

            if(!m.containsKey(s.charAt(j))){
                m.put(s.charAt(j),m.getOrDefault(s.charAt(j),0)+1);
                j++;
            }
            else{
                max = Math.max(max,j-i);
                m.put(s.charAt(i),m.get(s.charAt(i))-1);
                if(m.get(s.charAt(i))==0){
                    m.remove(s.charAt(i));
                }
                i++;
            }
         }
         return Math.max(max,j-i);
         
        
    }
}
