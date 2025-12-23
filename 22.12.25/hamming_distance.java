class Solution {
    public int hammingDistance(int x, int y) {
     int xor = x ^ y; // XOR to find differing bits
        int count = 0;
        while (xor != 0) {
            count += xor & 1; // add 1 if last bit is 1
            xor >>= 1;        // shift right
        }
        return count;   
    }
}
