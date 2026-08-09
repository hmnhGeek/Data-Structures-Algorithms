package DynamicProgramming.DP39;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(2n) and space complexity is O(2n).
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Map<Boolean, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n + 1; i += 1) {
            Map<Boolean, Integer> next = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                next.put(j, 0);
            }
            dp.put(i, next);
        }
        for (int i = n - 1; i >= 0; i -= 1) {
            for (Boolean j : List.of(true, false)) {
                if (j) {
                    dp.get(i).put(j, Math.max(
                            -arr.get(i) + dp.get(i + 1).get(!j),
                            dp.get(i + 1).get(j)
                    ));
                } else {
                    dp.get(i).put(j, Math.max(
                            arr.get(i) + dp.get(i + 2).get(!j),
                            dp.get(i + 1).get(j)
                    ));
                }
            }
        }
        return dp.get(0).get(true);
    }
}
