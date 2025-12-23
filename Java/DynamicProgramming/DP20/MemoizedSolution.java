package DynamicProgramming.DP20;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(target + n * target).
     */
    public static Integer getMinCoins(List<Integer> denominations, Integer target) {
        int n = denominations.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> subDp = new HashMap<>();
            for (int j = 0; j <= target; j += 1) {
                subDp.put(j, null);
            }
            dp.put(i, subDp);
        }
        Integer count = solve(denominations, n - 1, target, dp);
        if (count == Integer.MAX_VALUE) return -1;
        return count;
    }

    private static Integer solve(List<Integer> denominations, Integer i, Integer j, Map<Integer, Map<Integer, Integer>> dp) {
        if (j == 0) return 0;
        if (i == 0) {
            if (j % denominations.getFirst() == 0) {
                return j / denominations.getFirst();
            }
            return Integer.MAX_VALUE;
        }
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        Integer left = Integer.MAX_VALUE;
        if (j >= denominations.get(i)) {
            Integer subCoinsCount = solve(denominations, i, j - denominations.get(i), dp);
            if (subCoinsCount != Integer.MAX_VALUE) {
                left = 1 + subCoinsCount;
            }
        }
        Integer right = solve(denominations,  i - 1, j, dp);
        dp.get(i).put(j, Math.min(left, right));
        return dp.get(i).get(j);
    }
}
