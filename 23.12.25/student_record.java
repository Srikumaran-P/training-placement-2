class Solution {
    public boolean checkRecord(String s) {
        boolean r = false;
        int A = 0;
        int L = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'A') A++;
            if (A >= 2) return false;
            if (s.charAt(i) == 'L') L++;
            if (L >= 3) return false;
            if (s.charAt(i) == 'A' || s.charAt(i) == 'P') L = 0;
        }
        return true;
    }
}
