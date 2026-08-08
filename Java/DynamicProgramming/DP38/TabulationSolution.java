package DynamicProgramming.DP38;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n * k) and space complexity is O(n * k).
     */
    public static Integer getMaxProfit(List<Integer> arr, Integer maxTransactions) {
        int n = arr.size();
        Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Boolean, Map<Integer, Integer>> subMap1 = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                Map<Integer, Integer> subMap2 = new HashMap<>();
                for (int p = 0; p <= maxTransactions; p += 1) {
                    subMap2.put(p, 0);
                }
                subMap1.put(j, subMap2);
            }
            dp.put(i, subMap1);
        }

        for (int i = n - 1; i >= 0; i -= 1) {
            for (Boolean j : List.of(true, false)) {
                for (int k = 1; k <= maxTransactions; k += 1) {
                    if (j) {
                        dp.get(i).get(j).put(k, Math.max(
                                -arr.get(i) + dp.get(i + 1).get(!j).get(k),
                                dp.get(i + 1).get(j).get(k)
                        ));
                    } else {
                        dp.get(i).get(j).put(k, Math.max(
                                arr.get(i) + dp.get(i + 1).get(!j).get(k - 1),
                                dp.get(i + 1).get(j).get(k)
                        ));
                    }
                }
            }
        }

        return dp.get(0).get(true).get(maxTransactions);
    }
}
