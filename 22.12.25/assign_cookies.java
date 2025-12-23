class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int gi = 0, si = 0;
        int result = 0;
        Arrays.sort(g);
        Arrays.sort(s);
        while (gi < g.length && si < s.length) {
            if (g[gi] <= s[si]) {
                result++;
                gi++;
                si++;
            } else {
                si++;
            }
        }
        return result;
    }
}
