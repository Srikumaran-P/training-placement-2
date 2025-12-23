class Solution {
    public String[] findWords(String[] words) {
        return Arrays.stream(words).filter(w -> w.toLowerCase().chars().mapToObj(c -> "qwertyuiop|asdfghjkl|zxcvbnm".indexOf(c)).map(i -> i < 10 ? 0 : i < 21 ? 1 : 2).distinct().count() == 1).toArray(String[]::new);

        

        
    }
}
