package DynamicProgramming.DP36;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n) and space complexity is O(n).
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Map<Boolean, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Boolean, Integer> subMap = new HashMap<>();
            subMap.put(true, 0);
            subMap.put(false, 0);
            dp.put(i, subMap);
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
                            arr.get(i) + dp.get(i + 1).get(!j),
                            dp.get(i + 1).get(j)
                    ));
                }
            }
        }
        return dp.get(0).get(true);
    }
}
