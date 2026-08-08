package DynamicProgramming.DP38;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static Integer getMaxProfit(List<Integer> arr, Integer k) {
        int n = arr.size();
        return solve(arr, 0, true, k, n);
    }

    private static Integer solve(List<Integer> arr, int i, boolean j, int k, int n) {
        if (i >= n) return 0;
        if (k == 0) return 0;
        if (j) {
            return Math.max(
                    -arr.get(i) + solve(arr, i + 1, !j, k, n),
                    solve(arr, i + 1, j, k, n)
            );
        } else {
            return Math.max(
                    arr.get(i) + solve(arr, i + 1, !j, k - 1, n),
                    solve(arr, i + 1, j, k, n)
            );
        }
    }
}
