package DynamicProgramming.DP23;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(nk) and space complexity is O(nk).
     */
    public static Integer getUnboundedKnapsack(List<Integer> weights, List<Integer> values, Integer capacity) {
        if (capacity < 0 || weights.size() != values.size()) return null;
        int n = weights.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j < capacity + 1; j += 1) {
                prev.put(j, 0);
            }
            dp.put(i, prev);
        }
        for (int j = 0; j < capacity + 1; j += 1) {
            if (j % weights.getFirst() == 0) {
                dp.get(0).put(j, (j / weights.getFirst()) * values.getFirst());
            }
        }

        for (int i = 1; i < n; i += 1) {
            for (int j = 0; j < capacity + 1; j += 1) {
                Integer left = Integer.MIN_VALUE;
                if (j >= weights.get(i)) {
                    left = values.get(i) + dp.get(i).get(j - weights.get(i));
                }
                Integer right = dp.get(i - 1).get(j);
                dp.get(i).put(j, Math.max(left, right));
            }
        }
        return dp.get(n - 1).get(capacity);
    }
}
