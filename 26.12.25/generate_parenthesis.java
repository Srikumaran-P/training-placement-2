class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        backtrack(ans, "", 0, 0, n);
        return ans;
    }

    private void backtrack(List<String> ans, String curr, int open, int close, int n) {
        // valid string ban gaya
        if (curr.length() == 2 * n) {
            ans.add(curr);
            return;
        }

        // open bracket add kar sakte hain
        if (open < n) {
            backtrack(ans, curr + "(", open + 1, close, n);
        }

        // close bracket tabhi add karenge jab valid ho
        if (close < open) {
            backtrack(ans, curr + ")", open, close + 1, n);
        }
    }
}
