package DynamicProgramming.DP39;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(2n) and space complexity is O(1).
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();

        Map<Boolean, Integer> next = new HashMap<>();
        for (Boolean j : List.of(true, false)) {
            next.put(j, 0);
        }
        Map<Boolean, Integer> next2 = new HashMap<>();
        for (Boolean j : List.of(true, false)) {
            next2.put(j, 0);
        }

        for (int i = n - 1; i >= 0; i -= 1) {
            Map<Boolean, Integer> curr = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                curr.put(j, 0);
            }
            for (Boolean j : List.of(true, false)) {
                if (j) {
                    curr.put(j, Math.max(
                            -arr.get(i) + next.get(!j),
                            next.get(j)
                    ));
                } else {
                    curr.put(j, Math.max(
                            arr.get(i) + next2.get(!j),
                            next.get(j)
                    ));
                }
            }
            next2 = next;
            next = curr;
        }
        return next.get(true);
    }
}
