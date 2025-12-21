class Solution {
    public String longestCommonPrefix(String[] strs) {
        // Handle edge case: empty array
        if (strs == null || strs.length == 0) {
            return "";
        }

        // Sort the array to group similar strings
        Arrays.sort(strs);

        // We only need to compare the first and the last string
        // because the array is sorted.
        String first = strs[0];
        String last = strs[strs.length - 1];
        
        StringBuilder ans = new StringBuilder();

        // Iterate through the length of the shorter string
        for (int i = 0; i < Math.min(first.length(), last.length()); i++) {
            
            // If characters don't match, the prefix ends here
            if (first.charAt(i) != last.charAt(i)) {
                return ans.toString();
            }

            // Append matching character
            ans.append(first.charAt(i));
        }

        return ans.toString();
    }
}
