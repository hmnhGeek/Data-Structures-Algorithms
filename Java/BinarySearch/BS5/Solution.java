// Problem link - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
// Solution - https://www.youtube.com/watch?v=w2G2W8l__pc&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=6


package BinarySearch.BS5;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Boolean findInRotatedSortedArray(List<Integer> arr, Integer x) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        Integer low = 0, high = arr.size() - 1;
        while (low <= high) {
            Integer mid = (low + (high - low)/2);
            if (arr.get(mid).equals(x)) return true;
            if (arr.get(mid) == arr.get(low) && arr.get(mid) == arr.get(high)) {
                low += 1;
                high -= 1;
                continue;
            }
            if (arr.get(mid) <= arr.get(high)) {
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
        return false;
    }

    public static void main(String[] args) {
        System.out.println(findInRotatedSortedArray(Arrays.asList(3, 1, 2, 3, 3, 3, 3), 3));
        System.out.println(findInRotatedSortedArray(Arrays.asList(3, 1, 2, 3, 3, 3, 3), 4));
        System.out.println(findInRotatedSortedArray(Arrays.asList(2,5,6,0,0,1,2), 0));
        System.out.println(findInRotatedSortedArray(Arrays.asList(2,5,6,0,0,1,2), 3));
    }
}
