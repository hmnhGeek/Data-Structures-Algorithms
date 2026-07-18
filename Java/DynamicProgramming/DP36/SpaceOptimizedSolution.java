package DynamicProgramming.DP36;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n) and space complexity is O().
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        Map<Boolean, Integer> next = new HashMap<>();
        next.put(true, 0);
        next.put(false, 0);
        for (int i = n - 1; i >= 0; i -= 1) {
            Map<Boolean, Integer> curr = new HashMap<>();
            curr.put(true, 0);
            curr.put(false, 0);
            for (Boolean j : List.of(true, false)) {
                if (j) {
                    curr.put(j, Math.max(
                            -arr.get(i) + next.get(!j),
                            next.get(j)
                    ));
                } else {
                    curr.put(j, Math.max(
                            arr.get(i) + next.get(!j),
                            next.get(j)
                    ));
                }
            }
            next = curr;
        }
        return next.get(true);
    }
}
