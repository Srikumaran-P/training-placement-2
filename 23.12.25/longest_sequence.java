class Solution {
    public int findLUSlength(String a, String b) {
        if (a.length() == 0 || b.length() == 0)
            return -1;

        if (a.length() > b.length()) {
            return a.length();
        } else if (a.length() < b.length()){
            return b.length();
        } else {
            if (!a.contains(b)) {
                return a.length();
            } else {
                return -1;
            }
        }     
    }
}
