class Solution {
    public String convertToBase7(int num) {
        if(num==0){
            return "0";
        }
        // handle negative numbers
        boolean negative = false;
        if (num < 0) {
            negative = true;
            num = Math.abs(num);//convert negative number into positive number
        }

        StringBuilder sb = new StringBuilder();

        // convert to base 7
        while (num > 0) {
            int rem = num % 7;
            sb.append(rem);
            num = num / 7;
        }
        if (negative) {
            sb.append("-");
        }
        return sb.reverse().toString();
    }
}
