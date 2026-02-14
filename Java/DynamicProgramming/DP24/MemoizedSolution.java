package DynamicProgramming.DP24;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n + n^2).
     */
    public static Integer getMaxCost(List<Integer> prices) {
        int n = prices.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j <= n; j += 1) {
                prev.put(j, null);
            }
            dp.put(i, prev);
        }
        return solve(prices, n - 1, n, dp);
    }

    private static Integer solve(List<Integer> prices, int i, int j, Map<Integer, Map<Integer, Integer>> dp) {
        if (j == 0) return 0;
        if (i == 0) {
            return j * prices.getFirst();
        }
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        Integer left = Integer.MIN_VALUE;
        if (i + 1 <= j) {
            left = prices.get(i) + solve(prices, i, j - i - 1, dp);
        }
        Integer right = solve(prices, i - 1, j, dp);
        dp.get(i).put(j, Math.max(left, right));
        return dp.get(i).get(j);
    }
}
