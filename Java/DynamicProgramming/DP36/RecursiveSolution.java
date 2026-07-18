package DynamicProgramming.DP36;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        return solve(arr, 0, true, n);
    }

    private static Integer solve(List<Integer> arr, int i, boolean j, int n) {
        if (i == n) return 0;
        if (j) {
            return Math.max(
                    -arr.get(i) + solve(arr, i + 1, !j, n),
                    solve(arr, i + 1, j, n)
            );
        } else {
            return Math.max(
                    arr.get(i) + solve(arr, i + 1, !j, n),
                    solve(arr, i + 1, j, n)
            );
        }
    }
}
