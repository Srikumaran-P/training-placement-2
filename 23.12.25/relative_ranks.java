class Solution {
    public String[] findRelativeRanks(int[] score) {
        if (score.length == 0)
            return new String[0];

        String[] res = new String[score.length];

        int[] copied = Arrays.copyOf(score, score.length);
        Arrays.sort(copied);
        for (int i = 0; i < score.length; i++) {
            if (score[i] == copied[copied.length-1]) {
                res[i] = "Gold Medal";
            } else if (copied.length > 1 && score[i] == copied[copied.length-2]) {
                res[i] = "Silver Medal";
            } else if (copied.length > 2 && score[i] == copied[copied.length-3]) {
                res[i] = "Bronze Medal";
            } else {
                res[i] = String.valueOf(copied.length - Arrays.binarySearch(copied, score[i]));
            }
        }

        return res;      
    }
}
