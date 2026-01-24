package DynamicProgramming.DP22;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(nk) and space complexity O(n + nk).
     */
    public static Integer getNumWays(List<Integer> coins, Integer target) {
        if (target < 0) return null;
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < coins.size(); i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int k = 0; k < target + 1; k += 1) {
                prev.put(k, null);
            }
            dp.put(i, prev);
        }
        return solve(coins, target, coins.size() - 1, dp);
    }

    private static Integer solve(List<Integer> coins, Integer k, Integer i, Map<Integer, Map<Integer, Integer>> dp) {
        if (k == 0) return 1;
        if (i == 0) {
            if (k % coins.getFirst() == 0) return 1;
            return 0;
        }
        if (dp.get(i).get(k) != null) {
            return dp.get(i).get(k);
        }
        Integer left = 0;
        if (coins.get(i) <= k) {
            left = solve(coins, k - coins.get(i), i, dp);
        }
        Integer right = solve(coins, k, i - 1, dp);
        dp.get(i).put(k, left + right);
        return dp.get(i).get(k);
    }
}
