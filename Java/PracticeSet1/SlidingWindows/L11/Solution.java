// Problem link - https://www.naukri.com/code360/problems/subarrays-with-at-most-k-distinct-values_1473804
// Solution - https://www.youtube.com/watch?v=7wYGbV_LsX4&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=11


package PracticeSet1.SlidingWindows.L11;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static Integer getLessThanCount(List<Integer> arr, Integer k) {
        if (k < 0) return 0;
        int n = arr.size(), left = 0, right = 0, count = 0;
        Map<Integer, Integer> d = new HashMap<>();
        for (Integer i : arr) {
            d.put(i, 0);
        }
        while (right < n) {
            d.put(arr.get(right), d.get(arr.get(right)) + 1);
            while (getUniqueCount(d) > k) {
                d.put(arr.get(left), d.get(arr.get(left)) - 1);
                left += 1;
            }
            count += (right - left + 1);
            right += 1;
        }
        return count;
    }

    private static int getUniqueCount(Map<Integer, Integer> d) {
        int count = 0;
        for (Integer i : d.keySet()) {
            if (d.get(i) > 0) {
                count += 1;
            }
        }
        return count;
    }

    public static Integer getSubArrayCountWithKDifferentIntegers(List<Integer> arr, Integer k) {
        // Time complexity is O(2n) and space complexity is O(n).
        return Solution.getLessThanCount(arr, k) - Solution.getLessThanCount(arr, k - 1);
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.getSubArrayCountWithKDifferentIntegers(
                        List.of(2, 1, 1, 1, 3, 4, 3, 2), 3
                )
        );

        System.out.println(
                Solution.getSubArrayCountWithKDifferentIntegers(
                        List.of(1, 2, 1, 2, 3), 2
                )
        );

        System.out.println(
                Solution.getSubArrayCountWithKDifferentIntegers(
                        List.of(1, 2, 1, 3, 4), 3
                )
        );

        System.out.println(
                Solution.getSubArrayCountWithKDifferentIntegers(
                        List.of(2, 1, 2, 1, 6), 2
                )
        );

        System.out.println(
                Solution.getSubArrayCountWithKDifferentIntegers(
                        List.of(1, 2, 3, 4, 5), 1
                )
        );

        System.out.println(
                Solution.getSubArrayCountWithKDifferentIntegers(
                        List.of(2, 1, 3, 2, 4), 2
                )
        );

        System.out.println(
                Solution.getSubArrayCountWithKDifferentIntegers(
                        List.of(1, 2, 3, 4, 5), 4
                )
        );
    }
}
