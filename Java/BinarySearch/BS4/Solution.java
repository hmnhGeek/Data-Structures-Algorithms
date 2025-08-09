// Problem link - https://leetcode.com/problems/search-in-rotated-sorted-array/description/
// Solution - https://www.youtube.com/watch?v=5qGrJbHhqFs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=5


package BinarySearch.BS4;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer findInRotatedSortedArray(List<Integer> arr, Integer x) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        Integer low = 0, high = arr.size() - 1;
        while (low <= high) {
            Integer mid = (low + (high - low)/2);
            if (arr.get(mid).equals(x)) return mid;
            else if (arr.get(mid) <= arr.get(high)) {
                if (arr.get(mid) <= x && x <= arr.get(high)) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            } else if (arr.get(low) <= x && x <= arr.get(mid)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(findInRotatedSortedArray(Arrays.asList(7, 8, 9, 1, 2, 3, 4, 5, 6), 1));
        System.out.println(findInRotatedSortedArray(Arrays.asList(7, 8, 9, 1, 2, 3, 4, 5), 6));
        System.out.println(findInRotatedSortedArray(Arrays.asList(4,5,6,7,0,1,2), 0));
        System.out.println(findInRotatedSortedArray(Arrays.asList(4,5,6,7,0,1,2), 3));
        System.out.println(findInRotatedSortedArray(Arrays.asList(1), 0));
    }
}
