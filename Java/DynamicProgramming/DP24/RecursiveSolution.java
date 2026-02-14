package DynamicProgramming.DP24;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static Integer getMaxCost(List<Integer> prices) {
        int n = prices.size();
        return solve(prices, n - 1, n);
    }

    private static Integer solve(List<Integer> prices, int i, int j) {
        if (j == 0) return 0;
        if (i == 0) {
            return j * prices.getFirst();
        }
        Integer left = Integer.MIN_VALUE;
        if (i + 1 <= j) {
            left = prices.get(i) + solve(prices, i, j - i - 1);
        }
        Integer right = solve(prices, i - 1, j);
        return Math.max(left, right);
    }
}
