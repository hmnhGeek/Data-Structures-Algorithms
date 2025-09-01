// Problem link - https://leetcode.com/problems/subarrays-with-k-different-integers/description/
// Solution - https://www.youtube.com/watch?v=7wYGbV_LsX4&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=11


package SlidingWindows.L11;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static Map<Integer, Integer> getMap(List<Integer> arr) {
        Map<Integer, Integer> d = new HashMap<>();
        for (Integer i : arr) {
            d.put(i, 0);
        }
        return d;
    }

    private static Integer getLessThanEqualsTo(List<Integer> arr, Integer k) {
        if (k < 0) return 0;
        int left = 0, right = 0;
        int n = arr.size();
        Map<Integer, Integer> d = getMap(arr);
        int count = 0;

        while (right < n) {
            d.put(arr.get(right), d.get(arr.get(right)) + 1);
            while (invalidCondition(d, k)) {
                d.put(arr.get(left), d.get(arr.get(left)) - 1);
                left += 1;
            }
            count += (right - left + 1);
            right += 1;
        }
        return count;
    }

    private static boolean invalidCondition(Map<Integer, Integer> d, Integer k) {
        int count = 0;
        for (Integer i : d.keySet()) {
            if (d.get(i) > 0) {
                count += 1;
            }
        }
        return count > k;
    }

    public static Integer getSubArrayCount(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        return getLessThanEqualsTo(arr, k) - getLessThanEqualsTo(arr, k - 1);
    }

    public static void main(String[] args) {
        System.out.println(getSubArrayCount(Arrays.asList(1, 2, 1, 3, 4), 3));
        System.out.println(getSubArrayCount(Arrays.asList(1, 2, 1, 2, 3), 2));
        System.out.println(getSubArrayCount(Arrays.asList(1, 2, 3, 4, 5), 1));
        System.out.println(getSubArrayCount(Arrays.asList(2, 1, 3, 2, 4), 2));
        System.out.println(getSubArrayCount(Arrays.asList(1, 2, 3, 4, 5), 4));
    }
}
