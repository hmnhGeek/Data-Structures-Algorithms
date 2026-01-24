package DynamicProgramming.DP23;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(nk) and space complexity is O(k).
     */
    public static Integer getUnboundedKnapsack(List<Integer> weights, List<Integer> values, Integer capacity) {
        if (capacity < 0 || weights.size() != values.size()) return null;
        int n = weights.size();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j < capacity + 1; j += 1) {
            prev.put(j, 0);
        }
        for (int j = 0; j < capacity + 1; j += 1) {
            if (j % weights.getFirst() == 0) {
                prev.put(j, (j / weights.getFirst()) * values.getFirst());
            }
        }
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j < capacity + 1; j += 1) {
                curr.put(j, 0);
            }
            for (int j = 0; j < capacity + 1; j += 1) {
                Integer left = Integer.MIN_VALUE;
                if (j >= weights.get(i)) {
                    left = values.get(i) + curr.get(j - weights.get(i));
                }
                Integer right = prev.get(j);
                curr.put(j, Math.max(left, right));
            }
            prev = curr;
        }
        return prev.get(capacity);
    }
}
