package DynamicProgramming.DP23;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(nk) and space complexity is O(n + nk).
     */
    public static Integer getUnboundedKnapsack(List<Integer> weights, List<Integer> values, Integer capacity) {
        if (capacity < 0 || weights.size() != values.size()) return null;
        int n = weights.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j < capacity + 1; j += 1) {
                prev.put(j, null);
            }
            dp.put(i, prev);
        }
        return solve(weights, values, n - 1, capacity, dp);
    }

    private static Integer solve(List<Integer> weights, List<Integer> values, int i, Integer j, Map<Integer, Map<Integer, Integer>> dp) {
        if (j == 0) return 0;
        if (i == 0) {
            if (j % weights.getFirst() == 0) {
                return (j / weights.getFirst()) * values.getFirst();
            }
            return 0;
        }
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        Integer left = Integer.MIN_VALUE;
        if (j >= weights.get(i)) {
            left = values.get(i) + solve(weights, values, i, j - weights.get(i), dp);
        }
        Integer right = solve(weights, values, i - 1, j, dp);
        dp.get(i).put(j, Math.max(left, right));
        return dp.get(i).get(j);
    }
}
