package DynamicProgramming.DP19;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n*capacity) and space complexity is O(capacity).
     */
    public static Integer getKnapsack(List<Integer> weights, List<Integer> values, Integer capacity) {
        int n = weights.size();

        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j <= capacity; j += 1) {
            prev.put(j, 0);
        }

        for (int j = 0; j <= capacity; j += 1) {
            if (j >= weights.getFirst()) {
                prev.put(j, values.getFirst());
            }
        }

        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= capacity; j += 1) {
                curr.put(j, 0);
            }
            for (int j = 0; j <= capacity; j += 1) {
                Integer left = 0;
                if (j >= weights.get(i)) {
                    left = values.get(i) + prev.get(j - weights.get(i));
                }
                Integer right = prev.get(j);
                curr.put(j, Math.max(left, right));
            }
            prev = curr;
        }
        return prev.get(capacity);
    }
}
