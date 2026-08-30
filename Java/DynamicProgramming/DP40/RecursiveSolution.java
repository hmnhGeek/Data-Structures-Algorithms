package DynamicProgramming.DP40;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static Integer getMaxProfit(List<Integer> arr, Integer transactionFee) {
        int n = arr.size();
        return solve(arr, 0, true, transactionFee, n);
    }

    private static Integer solve(List<Integer> arr, int i, boolean j, Integer transactionFee, int n) {
        if (i >= n) return 0;
        if (j) {
            return Math.max(
                    -arr.get(i) + solve(arr, i + 1, !j, transactionFee, n),
                    solve(arr, i + 1, j, transactionFee, n)
            );
        } else {
            return Math.max(
                    arr.get(i) - transactionFee + solve(arr, i + 1, !j, transactionFee, n),
                    solve(arr, i + 1, j, transactionFee, n)
            );
        }
    }
}
