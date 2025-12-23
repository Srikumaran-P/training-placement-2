class Solution {
    public int[] constructRectangle(int area) {
    int w = (int) Math.sqrt(area); // start from sqrt(area)
        while (area % w != 0) {
            w--; // find the largest width that divides area
        }
        int l = area / w;
        return new int[]{l, w};
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.constructRectangle(4)));       // Output: [2, 2]
        System.out.println(Arrays.toString(sol.constructRectangle(37)));      // Output: [37, 1]
        System.out.println(Arrays.toString(sol.constructRectangle(122122)));  // Output: [427, 286]
    }
}     
