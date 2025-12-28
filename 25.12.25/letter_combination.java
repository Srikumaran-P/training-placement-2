class Solution {
    public List<String> letterCombinations(String digits) {
        return combo("",digits);
    }

     ArrayList<String> combo(String p, String up){
        if(up.isEmpty()){
            ArrayList<String> ls = new ArrayList<>();
            ls.add(p);
            return ls;
        }

        ArrayList<String> ans = new ArrayList<>();
        int digit = up.charAt(0) - '0';
        String chars = "";
        switch (digit) {
            case 2: chars = "abc"; break;
            case 3: chars = "def"; break;
            case 4: chars = "ghi"; break;
            case 5: chars = "jkl"; break;
            case 6: chars = "mno"; break;
            case 7: chars = "pqrs"; break;
            case 8: chars = "tuv"; break;
            case 9: chars = "wxyz"; break;
            default: chars = ""; // for 0 or 1
        }

        for(int i = 0; i < chars.length();i++){
            char ch = chars.charAt(i);
            ans.addAll(combo(p+ch,up.substring(1)));
        }

        return ans;
    }
}
