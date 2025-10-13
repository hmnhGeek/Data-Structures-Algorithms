// Problem link - https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
// Solution - https://www.youtube.com/watch?v=rjEJeYCasHs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=12


package BinarySearch.BS11;

public class Solution {
    private static int binarySearchConditionValidator(int mid, int n, int x) {
        int result = 1;
        for (int i = 0; i < n; i += 1) {
            result = result * mid;
            if (result > x) return 1;
        }
        if (result == x) return 0;
        return -1;
    }

    public static Integer findNthRoot(Integer x, Integer n) {
        /*
            Time complexity is O(log(x) * n) and space complexity is O(1).
         */
        if (n < 0 || x < 0) return -1;
        int low = 0, high = x;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int midResult = binarySearchConditionValidator(mid, n, x);
            if (midResult == 0) return mid;
            if (midResult == 1) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(findNthRoot(27, 3));
        System.out.println(findNthRoot(9, 3));
        System.out.println(findNthRoot(625, 4));
    }
}
