package DynamicProgramming.DP35;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n)
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        return solve(arr, 0, true, 1, n);
    }

    private static Integer solve(List<Integer> arr, int i, boolean canBuy, int j, int n) {
        if (j <= 0) return 0;
        if (i >= n) return 0;
        if (canBuy) {
            return Math.max(
                    -arr.get(i) + solve(arr, i + 1, false, j, n),
                    solve(arr, i + 1, true, j, n)
            );
        } else {
            return Math.max(
                    arr.get(i) + solve(arr, i + 1, true, j - 1, n),
                    solve(arr, i + 1, false, j, n)
            );
        }
    }
}
