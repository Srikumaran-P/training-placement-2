public class Solution {
    public int countSegments(String s) {
        int count = 0;
        boolean inSegment = false;
        for (char c : s.toCharArray()) {
            if (c != ' ') {
                if (!inSegment) {
                    count++;
                    inSegment = true;
                }
            } else {
                inSegment = false;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String test = "Hello, my name is John";
        System.out.println(sol.countSegments(test)); // Output: 5
    }
}
