// Problem link - https://www.youtube.com/watch?v=Bsv3FPUX_BA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=11


package BinarySearch.BS10;

public class Solution {
    public static Integer findSqrt(Integer number) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */

        int low = 0, high = number;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (mid * mid == number) return mid;
            if (mid * mid < number) {
                low = mid + 1;
            } else {
                high = mid - 1;
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
