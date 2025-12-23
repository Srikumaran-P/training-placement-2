class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int row = mat.length;
        int col = mat[0].length;

        int newMat [][] = new int[r][c]; 
        if((row*col) != (r*c) ) return mat;
           
        else{
            ArrayList<Integer> myList = new ArrayList<>();
            for(int i = 0;i<row;i++){
                for(int j =0;j<col;j++){
                    myList.add(mat[i][j]);
                }
            }
            int count =0;
            for(int i =0;i<r;i++){
                for(int j =0;j<c;j++ ){  
                   newMat[i][j] = myList.get(count);
                    count++;
                }
            }
        }
        return newMat;
    }
}
