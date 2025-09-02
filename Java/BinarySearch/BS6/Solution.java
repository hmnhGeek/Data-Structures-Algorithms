// Problem link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Solution - https://www.youtube.com/watch?v=nhEMDKMB44g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=7


package BinarySearch.BS6;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getMinValue(List<Integer> arr) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        int low = 0, high = arr.size() - 1;
        Integer ans = Integer.MAX_VALUE;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(low) <= arr.get(mid)) {
                // this means left part is sorted. Pick minimum value from left part.
                ans = Math.min(ans, arr.get(low));
                low = mid + 1;
            } else {
                // this means right part is sorted.
                ans = Math.min(ans, arr.get(mid));
                high = mid - 1;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(getMinValue(Arrays.asList(4, 5, 6, 7, 0, 1, 2)));
        System.out.println(getMinValue(Arrays.asList(4, 1, 2, 3)));
        System.out.println(getMinValue(Arrays.asList(3, 4, 5, 1, 2)));
        System.out.println(getMinValue(Arrays.asList(3, 4, 1, 2)));
        System.out.println(getMinValue(Arrays.asList(25, 30, 5, 10, 15, 20)));
        System.out.println(getMinValue(Arrays.asList(11, 13, 15, 17)));
        System.out.println(getMinValue(Arrays.asList(7, 8, 1, 2, 3, 4, 5, 6)));
        System.out.println(getMinValue(Arrays.asList(1, 2)));
        System.out.println(getMinValue(Arrays.asList(2, 1)));
        System.out.println(getMinValue(Arrays.asList(3, 3, 3, 3, 3)));
        System.out.println(getMinValue(Arrays.asList(1, 2, 2, 3, 3, 3, 5)));
        System.out.println(getMinValue(Arrays.asList(5, 5, 5, 5, 1, 2, 3, 3)));
    }
}
