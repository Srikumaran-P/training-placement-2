class Solution {
    public int[] plusOne(int[] digits) {
        List<Integer> ans = new ArrayList<>();

        int i = digits.length - 1;
        int carry = 0;
        while(i >= 0 || carry > 0){
            int x = (i ==  digits.length - 1) ? 1 : 0;
            int sum = (i >= 0) ? digits[i] + x + carry : carry;

            ans.add(sum % 10);
            carry = sum / 10;
            i--;
        }

        int l = ans.size();
        int[] result = new int[l];
        for(int j = 0; j < l ; j++){
            result[j] = ans.get(l - j - 1);
        }

        return result;
    }
}
