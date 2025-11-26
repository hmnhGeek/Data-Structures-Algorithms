package DynamicProgramming.DP19;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n*capacity) and space complexity is O(n + n*capacity).
     */
    public static Integer getKnapsack(List<Integer> weights, List<Integer> values, Integer capacity) {
        int n = weights.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j < capacity; j += 1) {
                subMap.put(j, null);
            }
            dp.put(i, subMap);
        }
        return solve(weights, values, n - 1, capacity, dp);
    }

    private static Integer solve(List<Integer> weights, List<Integer> values, int i, Integer j, Map<Integer, Map<Integer, Integer>> dp) {
        if (j == 0) {
            return 0;
        }
        if (i == 0) {
            if (j >= weights.getFirst()) return values.getFirst();
            return 0;
        }
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        Integer left = 0;
        if (j >= weights.get(i)) {
            left = values.get(i) + solve(weights, values, i - 1, j - weights.get(i), dp);
        }
        Integer right = solve(weights, values, i - 1, j, dp);
        dp.get(i).put(j, Math.max(left, right));
        return dp.get(i).get(j);
    }
}
