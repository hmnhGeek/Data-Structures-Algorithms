package DynamicProgramming.DP24;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n).
     */
    public static Integer getMaxCost(List<Integer> prices) {
        int n = prices.size();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j <= n; j += 1) {
            prev.put(j, Integer.MIN_VALUE);
        }
        prev.put(0, 0);
        for (int j = 0; j <= n; j += 1) {
            prev.put(j, j * prices.getFirst());
        }
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= n; j += 1) {
                curr.put(j, Integer.MIN_VALUE);
            }
            curr.put(0, 0);
            for (int j = 0; j <= n; j += 1) {
                Integer left = Integer.MIN_VALUE;
                if (i + 1 <= j) {
                    left = prices.get(i) + curr.get(j - i - 1);
                }
                Integer right = prev.get(j);
                curr.put(j, Math.max(left, right));
            }
            prev = curr;
        }
        return prev.get(n);
    }
}
