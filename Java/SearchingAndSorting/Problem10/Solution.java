// Problem link - https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1
// Solution - https://www.youtube.com/watch?v=5IUyc7cPD9E


package SearchingAndSorting.Problem10;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(detectPairs(Arrays.asList(5, 20, 3, 2, 5, 80), 78));
        System.out.println(detectPairs(Arrays.asList(90, 70, 20, 80, 50), 45));
        System.out.println(detectPairs(Arrays.asList(1), 1));
    }

    public static boolean detectPairs(List<Integer> arr, Integer target) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(1).
         */
        QuickSort.sort(arr);
        for (Integer i : arr) {
            if (isPresent(i + target, arr)) return true;
        }
        return false;
    }

    private static boolean isPresent(int i, List<Integer> arr) {
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            Integer elem = arr.get(mid);
            if (elem == i) return true;
            if (elem > i) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return false;
    }
}
