
class Solution {
    public int findKthNumber(int m, int n, int k) {
        int low = 1, high = m * n;
        while (low < high) {
            int mid = low + (high - low) / 2;//5
            int count = 0;//4 
            for (int i = 1; i <= m; i++) {
                count += Math.min(mid / i, n);//3 
            }
            if (count < k) {
                low = mid + 1;//4
            } else {
                high = mid;
            }
        }
        return low;
    }
}
