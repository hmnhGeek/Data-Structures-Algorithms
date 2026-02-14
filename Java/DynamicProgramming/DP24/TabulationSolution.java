package DynamicProgramming.DP24;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n^2).
     */
    public static Integer getMaxCost(List<Integer> prices) {
        int n = prices.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j <= n; j += 1) {
                prev.put(j, Integer.MIN_VALUE);
            }
            dp.put(i, prev);
        }
        for (int i = 0; i < n; i += 1) {
            dp.get(i).put(0, 0);
        }
        for (int j = 0; j <= n; j += 1) {
            dp.get(0).put(j, j * prices.getFirst());
        }
        for (int i = 1; i < n; i += 1) {
            for (int j = 0; j <= n; j += 1) {
                Integer left = Integer.MIN_VALUE;
                if (i + 1 <= j) {
                    left = prices.get(i) + dp.get(i).get(j - i - 1);
                }
                Integer right = dp.get(i - 1).get(j);
                dp.get(i).put(j, Math.max(left, right));
            }
        }
        return dp.get(n - 1).get(n);
    }
}
