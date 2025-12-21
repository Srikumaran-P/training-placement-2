class Solution {
    public String solveEquation(String equation) {
        String[] sides = equation.split("=");
        int[] left = parse(sides[0]);
        int[] right = parse(sides[1]);
        
        int xCoeff = left[0] - right[0];
        int constSum = right[1] - left[1];
        
        if (xCoeff == 0) {
            if (constSum == 0) return "Infinite solutions";
            else return "No solution";
        } else {
            int x = constSum / xCoeff;
            return "x=" + x;
        }
    }
    
    // returns int[]{xCoeff, constSum}
    private int[] parse(String s) {
        int xCoeff = 0, constSum = 0;
        int n = s.length();
        int i = 0;
        
        while (i < n) {
            int sign = 1;
            if (s.charAt(i) == '+' || s.charAt(i) == '-') {
                sign = s.charAt(i) == '+' ? 1 : -1;
                i++;
            }
            
            int j = i;
            while (j < n && Character.isDigit(s.charAt(j))) j++;
            
            if (j < n && s.charAt(j) == 'x') {
                int coeff = 0;
                if (i == j) coeff = 1; // "x" or "-x"
                else coeff = Integer.parseInt(s.substring(i, j));
                xCoeff += sign * coeff;
                i = j + 1;
            } else {
                if (i != j) {
                    int num = Integer.parseInt(s.substring(i, j));
                    constSum += sign * num;
                }
                i = j;
            }
        }
        
        return new int[]{xCoeff, constSum};
    }
}
