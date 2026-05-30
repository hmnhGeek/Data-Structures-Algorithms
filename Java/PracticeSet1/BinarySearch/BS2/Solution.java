// Problem link - https://www.naukri.com/code360/problems/lower-bound_8165382
// Problem link - https://www.naukri.com/code360/problems/implement-upper-bound_8165383
// Problem link - https://www.naukri.com/code360/problems/algorithm-to-find-best-insert-position-in-sorted-array_839813
// Solution - https://www.youtube.com/watch?v=6zhGS79oQ4k&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=3


package PracticeSet1.BinarySearch.BS2;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println("Lower Bound");
        System.out.println(getLowerBound(Arrays.asList(3, 5, 8, 15, 19), 10));
        System.out.println(getLowerBound(Arrays.asList(1, 2, 2, 3), 0));
        System.out.println(getLowerBound(Arrays.asList(1, 2, 2, 3, 3, 5), 0));
        System.out.println(getLowerBound(Arrays.asList(1, 2, 2, 3, 3, 5), 2));
        System.out.println(getLowerBound(Arrays.asList(1, 2, 2, 3, 3, 5), 7));
        System.out.println("Upper Bound");
        System.out.println(getUpperBound(Arrays.asList(2, 4, 6, 7), 5));
        System.out.println(getUpperBound(Arrays.asList(1, 4, 7, 8, 10), 7));
        System.out.println(getUpperBound(Arrays.asList(1, 2, 5, 6, 10), 10));
        System.out.println(getUpperBound(Arrays.asList(1, 5, 5, 7, 7, 9, 10), 5));
        System.out.println("Insert Position");
        System.out.println(getInsertPosition(Arrays.asList(1, 2, 2, 4, 7), 6));
        System.out.println(getInsertPosition(Arrays.asList(1, 2, 4, 7), 9));
        System.out.println(getInsertPosition(Arrays.asList(2, 5, 7), 1));
        System.out.println(getInsertPosition(Arrays.asList(1, 2, 4, 7), 2));
        System.out.println("Floor");
        System.out.println(getFloor(Arrays.asList(10, 20, 30, 40, 50), 25));
        System.out.println(getFloor(Arrays.asList(10, 20, 30, 40, 50), 30));
        System.out.println(getFloor(Arrays.asList(10, 20, 30, 40, 50), 15));
    }

    public static int getLowerBound(List<Integer> arr, Integer x) {
        /*
            Time complexity is O(log(arr.size())) and space complexity is O(1).
         */
        int n = arr.size();
        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) >= x) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    public static int getUpperBound(List<Integer> arr, Integer x) {
        /*
            Time complexity is O(log(arr.size())) and space complexity is O(1).
         */
        int n = arr.size();
        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) > x) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    public static int getInsertPosition(List<Integer> arr, Integer x) {
        return getLowerBound(arr, x);
    }

    public static int getCeil(List<Integer> arr, Integer x) {
        return getLowerBound(arr, x);
    }

    public static Integer getFloor(List<Integer> arr, Integer x) {
        /*
            Time complexity is O(log(arr.size())) and space complexity is O(1).
         */
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid).compareTo(x) > 0) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return 0 <= high && high < arr.size() ? arr.get(high) : null;
    }
}
