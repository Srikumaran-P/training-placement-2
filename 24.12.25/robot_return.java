class Solution {
    public boolean judgeCircle(String moves) {

        
        int countU = number('U',moves);
        int countD = number('D',moves);
        int countR = number('R',moves);
        int countL = number('L',moves);

        return countD == countU && countR == countL;

        
    }

    int number(char ch , String moves ){
        int count = 0;
        for(int i = 0 ; i < moves.length(); i++) {
            if(moves.charAt(i) == ch){
                count++;
            }
        }
        return count;
    }
}
