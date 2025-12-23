class Solution {
    public String reverseStr(String s, int k) {
        StringBuilder sb = new StringBuilder();
        int counter = 0;
        int remain = Math.min(s.length(), k);
        for (int i = 0; i < s.length(); ) {
            if (i % (2*k) == 0) {
                counter = 0;
            }

            if (counter < k) {
                for (int j = 0; j < remain; j++) {
                    sb.append(s.charAt(i + remain -1 - j));
                    counter++;
                }
            } else {
                for (int j = 0; j < remain; j++) {
                    sb.append(s.charAt(i + j));
                    counter++;
                }
            }

            i+=k;
            remain = s.length() < i + k ? s.length() - i : k;
        }

        return sb.toString();        
    }
}
