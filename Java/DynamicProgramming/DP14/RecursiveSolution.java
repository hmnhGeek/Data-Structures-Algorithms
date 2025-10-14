package DynamicProgramming.DP14;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static boolean subsetSum(List<Integer> arr, Integer k) {
        int n = arr.size();
        return solve(arr, n - 1, k);
    }

    public static boolean solve(List<Integer> arr, int i, int k) {
        if (k == 0) return true;
        if (i == 0) {
            if (arr.getFirst() == k) return true;
            return false;
        }
        boolean left = false;
        if (arr.get(i) <= k) {
            left = solve(arr, i - 1, k - arr.get(i));
        }
        boolean right = solve(arr, i - 1, k);
        return left || right;
    }
}
