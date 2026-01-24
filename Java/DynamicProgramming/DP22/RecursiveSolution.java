package DynamicProgramming.DP22;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity O(n).
     */
    public static Integer getNumWays(List<Integer> coins, Integer target) {
        if (target < 0) return null;
        return solve(coins, target, coins.size() - 1);
    }

    private static Integer solve(List<Integer> coins, Integer k, Integer i) {
        if (k == 0) return 1;
        if (i == 0) {
            if (k % coins.getFirst() == 0) return 1;
            return 0;
        }
        Integer left = 0;
        if (coins.get(i) <= k) {
            left = solve(coins, k - coins.get(i), i);
        }
        Integer right = solve(coins, k, i - 1);
        return left + right;
    }
}
