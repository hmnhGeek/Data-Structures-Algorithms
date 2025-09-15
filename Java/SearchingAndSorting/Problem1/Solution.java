// Problem link - https://www.naukri.com/code360/problems/first-and-last-position-of-an-element-in-sorted-array_1082549


package SearchingAndSorting.Problem1;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<Integer> arr = Arrays.asList(2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15);

        System.out.println(getOccurrences(arr, 2));
        System.out.println(getOccurrences(arr, 6));
        System.out.println(getOccurrences(arr, 8));
        System.out.println(getOccurrences(arr, 13));
        System.out.println(getOccurrences(arr, 11));
        System.out.println(getOccurrences(arr, 15));
        System.out.println(getOccurrences(arr, 16));
        System.out.println(getOccurrences(arr, 5));

        System.out.println(getOccurrences(Arrays.asList(1, 3, 5, 5, 5, 5, 67, 123, 125), 5));
        System.out.println(getOccurrences(Arrays.asList(1, 3, 5, 5, 5, 5, 7, 123, 125), 7));
        System.out.println(getOccurrences(Arrays.asList(1, 2, 3), 4));
    }

    private static int getLeftmostOccurrence(List<Integer> arr, Integer x) {
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) >= x) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        if (0 <= low && low < arr.size() && arr.get(low) == x) {
            return low;
        }
        return -1;
    }

    private static int getRightmostOccurrence(List<Integer> arr, Integer x) {
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) <= x) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        if (0 <= high && high < arr.size() && arr.get(high) == x) {
            return high;
        }
        return -1;
    }

    public static List<Integer> getOccurrences(List<Integer> arr, Integer x) {
        /**
         * Time complexity is O(2 * log(n)) and space complexity is O(1).
         */
        Integer leftmostIndex = getLeftmostOccurrence(arr, x);
        if (leftmostIndex == -1) return List.of(-1, -1);
        Integer rightmostIndex = getRightmostOccurrence(arr, x);
        return List.of(leftmostIndex, rightmostIndex);
    }
}
