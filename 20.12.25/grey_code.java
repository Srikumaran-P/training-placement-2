// semicolons : 1
class Solution {
    public List<Integer> grayCode(int n) {
        return IntStream.range(0, 1 << n).map(i -> i ^ (i >> 1)).boxed().toList();
    }
}
