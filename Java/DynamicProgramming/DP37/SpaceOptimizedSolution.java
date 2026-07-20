package DynamicProgramming.DP37;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer findMaxProfit(List<Integer> arr) {
        /*
            Time complexity is O(4n) and space complexity is O(4).
         */
        int n = arr.size();
        Map<Boolean, Map<Integer, Integer>> next = new HashMap<>();
        for (Boolean j : List.of(true, false)) {
            Map<Integer, Integer> sub = new HashMap<>();
            for (int k = 0; k <= 2; k += 1) {
                sub.put(k, 0);
            }
            next.put(j, sub);
        }

        for (int i = n - 1; i >= 0; i -= 1) {
            Map<Boolean, Map<Integer, Integer>> curr = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                Map<Integer, Integer> sub = new HashMap<>();
                for (int k = 0; k <= 2; k += 1) {
                    sub.put(k, 0);
                }
                curr.put(j, sub);
            }
            for (Boolean j : List.of(true, false)) {
                for (int k = 1; k <= 2; k += 1) {
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
        return next.get(true).get(2);
    }
}
