// Problem link - https://www.naukri.com/code360/problems/first-and-last-position-of-an-element-in-sorted-array_1082549
// Solution - https://www.youtube.com/watch?v=hjR1IYVx9lY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=4


package BinarySearch.BS3;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static <T extends Comparable<T>> Integer getFirstOccurrence(List<T> arr, T x) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid).compareTo(x) >= 0) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return 0 <= low && low < arr.size() ? low : -1;
    }

    public static <T extends Comparable<T>> Integer getLastOccurrence(List<T> arr, T x) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid).compareTo(x) <= 0) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return 0 <= high && high < arr.size() ? high : -1;
    }

    public static <T extends Comparable<T>> List<Integer> getOccurrences(List<T> arr, T x) {
        Integer first = getFirstOccurrence(arr, x);
        Integer last = getLastOccurrence(arr, x);
        if (arr.get(first) != x || arr.get(last) != x) return List.of(-1, -1);
        return List.of(first, last);
    }

    public static void main(String[] args) {
        System.out.println(getOccurrences(Arrays.asList(2, 4, 6, 8, 8, 8, 11, 13), 8));
        System.out.println(getOccurrences(Arrays.asList(0, 1, 1, 5), 1));
        System.out.println(getOccurrences(Arrays.asList(0, 0, 1, 1, 2, 2, 2, 2), 2));
        System.out.println(getOccurrences(Arrays.asList(1, 3, 3, 5), 2));
    }
}
