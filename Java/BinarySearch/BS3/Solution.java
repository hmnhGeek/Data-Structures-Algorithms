package BinarySearch.BS3;

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
                low = mid + 1
            } else {
                high = mid - 1;
            }
        }
        return 0 <= high && high < arr.size() ? high : -1;
    }
}
