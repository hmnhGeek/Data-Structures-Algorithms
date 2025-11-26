package DynamicProgramming.DP19;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n*capacity) and space complexity is O(n*capacity).
     */
    public static Integer getKnapsack(List<Integer> weights, List<Integer> values, Integer capacity) {
        int n = weights.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j <= capacity; j += 1) {
                subMap.put(j, 0);
            }
            dp.put(i, subMap);
        }

        for (int j = 0; j <= capacity; j += 1) {
            if (j >= weights.getFirst()) {
                dp.get(0).put(j, values.getFirst());
            }
        }

        for (int i = 1; i < n; i += 1) {
            for (int j = 0; j <= capacity; j += 1) {
                Integer left = 0;
                if (j >= weights.get(i)) {
                    left = values.get(i) + dp.get(i - 1).get(j - weights.get(i));
                }
                Integer right = dp.get(i - 1).get(j);
                dp.get(i).put(j, Math.max(left, right));
            }
        }
        return dp.get(n - 1).get(capacity);
    }
}
