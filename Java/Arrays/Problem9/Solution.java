// Problem link - https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1
// Solution - https://www.youtube.com/watch?v=30vDmZg5MZ8


package Arrays.Problem9;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer minimizeHeights(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(1).
         */
        if (k <= 0) return null;
        QuickSort.sort(arr);

        // store the max ans in min `ans` variable for now.
        Integer ans = arr.getLast() - arr.getFirst();

        // we will always increase the 0th value and shrink the last value.
        Integer smallest = arr.getFirst() + k, largest = arr.getLast() - k;

        // initialize tracking variables.
        Integer mi = 0, mx = 0;

        // update logic (moving the pivot; i denotes pivot index)
        for (int i = 0; i < arr.size() - 1; i += 1) {
            // update `mi` based on the pivot index
            mi = Math.min(smallest, arr.get(i + 1) - k);
            // do the same for `mx`.
            mx = Math.max(largest, arr.get(i) + k);

            // we will not take negative heights
            if (mi < 0) continue;

            // update the answer.
            ans = Math.min(ans, mx - mi);
        }

        // return the answer.
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(minimizeHeights(Arrays.asList(1, 5, 8, 10), 2));
        System.out.println(minimizeHeights(Arrays.asList(3, 9, 12, 16, 20), 3));
        System.out.println(minimizeHeights(Arrays.asList(12, 6, 4, 15, 17, 10), 6));
        System.out.println(minimizeHeights(Arrays.asList(1, 5, 10, 15), 3));
    }
}
