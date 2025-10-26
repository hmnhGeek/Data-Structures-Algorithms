// Problem link - https://leetcode.com/problems/search-in-rotated-sorted-array/description/
// Solution - https://www.youtube.com/watch?v=5qGrJbHhqFs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=5


package SearchingAndSorting.Problem3;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static int search(List<Integer> list, Integer target) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        int low = 0, high = list.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (list.get(mid) == target) {
                return mid;
            }
            if (list.get(low) <= list.get(mid)) {
                if (list.get(low) <= target && target <= list.get(mid)) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if (list.get(mid) <= target && target <= list.get(high)) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(search(Arrays.asList(4, 5, 6, 7, 0, 1, 2), 0));
        System.out.println(search(Arrays.asList(4,5,6,7,0,1,2), 3));
        System.out.println(search(Arrays.asList(1), 0));
        System.out.println(search(Arrays.asList(7, 8, 9, 1, 2, 3, 4, 5, 6), 1));
        System.out.println(search(Arrays.asList(7, 8, 9, 1, 2, 3, 4, 5), 6));
    }
}
