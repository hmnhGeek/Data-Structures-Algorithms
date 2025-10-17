package DynamicProgramming.DP15;

import java.util.List;
import java.util.Objects;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(k).
     */
    public static boolean subsetSum(List<Integer> arr) {
        int n = arr.size();
        int k = arr.stream().mapToInt(Integer::intValue).sum();
        if (k % 2 != 0) return false;
        return solve(arr, n - 1, k / 2);
    }

    private static boolean solve(List<Integer> arr, int i, Integer k) {
        if (k == 0) return true;
        if (i == 0) return arr.getFirst() == k;
        boolean left = false;
        if (arr.get(i) <= k) {
            left = solve(arr, i - 1, k - arr.get(i));
        }
        boolean right = solve(arr, i - 1, k);
        return left || right;
    }
}
