package DynamicProgramming.DP38;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n * k) and space complexity is O(k).
     */
    public static Integer getMaxProfit(List<Integer> arr, Integer maxTransactions) {
        int n = arr.size();

        Map<Boolean, Map<Integer, Integer>> next = new HashMap<>();
        for (Boolean j : List.of(true, false)) {
            Map<Integer, Integer> subMap2 = new HashMap<>();
            for (int p = 0; p <= maxTransactions; p += 1) {
                subMap2.put(p, 0);
            }
            next.put(j, subMap2);
        }

        for (int i = n - 1; i >= 0; i -= 1) {
            Map<Boolean, Map<Integer, Integer>> curr = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                Map<Integer, Integer> subMap2 = new HashMap<>();
                for (int p = 0; p <= maxTransactions; p += 1) {
                    subMap2.put(p, 0);
                }
                curr.put(j, subMap2);
            }
            for (Boolean j : List.of(true, false)) {
                for (int k = 1; k <= maxTransactions; k += 1) {
                    if (j) {
                        curr.get(j).put(k, Math.max(
                                -arr.get(i) + next.get(!j).get(k),
                                next.get(j).get(k)
                        ));
                    } else {
                        curr.get(j).put(k, Math.max(
                                arr.get(i) + next.get(!j).get(k - 1),
                                next.get(j).get(k)
                        ));
                    }
                }
            }
            next = curr;
        }

        return next.get(true).get(maxTransactions);
    }
}
