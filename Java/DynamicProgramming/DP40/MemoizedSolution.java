package DynamicProgramming.DP40;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(2n) and space complexity is O(n + 2n).
     */
    public static Integer getMaxProfit(List<Integer> arr, Integer transactionFee) {
        int n = arr.size();
        Map<Integer, Map<Boolean, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Boolean, Integer> next = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                next.put(j, null);
            }
            dp.put(i, next);
        }
        return solve(arr, 0, true, transactionFee, n, dp);
    }

    private static Integer solve(List<Integer> arr, int i, boolean j, Integer transactionFee, int n, Map<Integer, Map<Boolean, Integer>> dp) {
        if (i >= n) return 0;
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        if (j) {
            dp.get(i).put(j, Math.max(
                    -arr.get(i) + solve(arr, i + 1, !j, transactionFee, n, dp),
                    solve(arr, i + 1, j, transactionFee, n, dp)
            ));
        } else {
            dp.get(i).put(j, Math.max(
                    arr.get(i) - transactionFee + solve(arr, i + 1, !j, transactionFee, n, dp),
                    solve(arr, i + 1, j, transactionFee, n, dp)
            ));
        }
        return dp.get(i).get(j);
    }
}
