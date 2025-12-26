// Problem link - https://www.geeksforgeeks.org/k-th-missing-element-in-sorted-array/
// Solution - https://www.youtube.com/watch?v=uZ0N_hZpyps&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=17


package BinarySearch.BS16;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer findMissingWholeNumber(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        if (k <= 0) return -1;
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) - mid - 1 < k) {
                low = mid + 1;
            } else if (arr.get(mid) - mid - 1 > k) {
                high = mid - 1;
            } else {
                high = mid - 1;
            }
        }
        return k + low;
    }

    public static void main(String[] args) {
        System.out.println(Solution.findMissingWholeNumber(Arrays.asList(2, 3, 4, 7, 11), 3));
        System.out.println(Solution.findMissingWholeNumber(Arrays.asList(2, 4, 5, 7), 3));
        System.out.println(Solution.findMissingWholeNumber(Arrays.asList(4, 7, 9, 10), 1));
        System.out.println(Solution.findMissingWholeNumber(Arrays.asList(4, 7, 9, 10), 4));
        System.out.println(Solution.findMissingWholeNumber(Arrays.asList(2, 3, 4, 7, 11), 5));
        System.out.println(Solution.findMissingWholeNumber(Arrays.asList(1, 2, 3, 4), 2));
        System.out.println(Solution.findMissingWholeNumber(Arrays.asList(3, 5, 9, 10, 11, 12), 2));
        System.out.println(Solution.findMissingWholeNumber(Arrays.asList(1, 2, 3), 2));
        System.out.println(Solution.findMissingWholeNumber(Arrays.asList(1, 2, 3), 0));
    }
}
