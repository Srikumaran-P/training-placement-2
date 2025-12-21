class Solution {
    
    public int romanToInt(String s) {
        
        int result = 0;

        for (int i = 0; i<s.length(); i++){
            
            char roman = s.charAt(i);
            char nextRoman = 'n';

            if (i < s.length()-1) {
                nextRoman = s.charAt(i+1);
            }

            int romanInt = RomanToInteger(roman);
            int nextRomanInt = RomanToInteger(nextRoman);

            if (romanInt >= nextRomanInt){
                result += romanInt;
            }
            else{
                result += nextRomanInt-romanInt;
                i++;
            }    
        }
        return result;
    }

    public int RomanToInteger(char roman){
        
        int romanInt = 0;

        switch (roman){
            case 'I':
                romanInt = 1;
            break;

            case 'V':
                romanInt = 5;
            break;

            case 'X':
                romanInt = 10;
            break;

            case 'L':
                romanInt = 50;
            break;

            case 'C':
                romanInt = 100;
            break;

            case 'D':
                romanInt = 500;
            break;

            case 'M':
                romanInt = 1000;
            break;

            case 'n':
                romanInt = 0;
            break;
        }
        return romanInt;
    }
}
