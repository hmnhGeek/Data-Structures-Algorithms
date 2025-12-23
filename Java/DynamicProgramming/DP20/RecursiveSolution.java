package DynamicProgramming.DP20;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(target).
     */
    public static Integer getMinCoins(List<Integer> denominations, Integer target) {
        int n = denominations.size();
        Integer count = solve(denominations, n - 1, target);
        if (count == Integer.MAX_VALUE) return -1;
        return count;
    }

    private static Integer solve(List<Integer> denominations, Integer i, Integer j) {
        if (j == 0) return 0;
        if (i == 0) {
            if (j % denominations.getFirst() == 0) {
                return j / denominations.getFirst();
            }
            return Integer.MAX_VALUE;
        }
        Integer left = Integer.MAX_VALUE;
        if (j >= denominations.get(i)) {
            Integer subCoinsCount = solve(denominations, i, j - denominations.get(i));
            if (subCoinsCount != Integer.MAX_VALUE) {
                left = 1 + subCoinsCount;
            }
        }
        Integer right = solve(denominations,  i - 1, j);
        return Math.min(left, right);
    }
}
