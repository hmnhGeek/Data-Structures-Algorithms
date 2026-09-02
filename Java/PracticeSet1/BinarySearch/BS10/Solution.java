// Problem link - https://www.youtube.com/watch?v=Bsv3FPUX_BA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=11


package PracticeSet1.BinarySearch.BS10;

public class Solution {
    public static Integer findSqrt(int n) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        if (n < 0) return null;
        if (n == 0) return 0;
        int low = 1, high = n;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (mid * mid == n) return mid;
            if (mid * mid > n) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return high;
    }

    public static void main(String[] args) {
        System.out.println(findSqrt(28));
        System.out.println(findSqrt(0));
        System.out.println(findSqrt(1));
        System.out.println(findSqrt(2));
        System.out.println(findSqrt(36));
        System.out.println(findSqrt(100));
    }
}
