package DynamicProgramming.DP37;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    public static Integer findMaxProfit(List<Integer> arr) {
        /*
            Time complexity is O(4n) and space complexity is O(4n).
         */
        int n = arr.size();
        Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int i = 0; i < n + 1; i += 1) {
            Map<Boolean, Map<Integer, Integer>> sub = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                Map<Integer, Integer> sub2 = new HashMap<>();
                for (int k = 0; k <= 2; k += 1) {
                    sub2.put(k, 0);
                }
                sub.put(j, sub2);
            }
            dp.put(i, sub);
        }
        for (int i = n - 1; i >= 0; i -= 1) {
            for (Boolean j : List.of(true, false)) {
                for (int k = 1; k <= 2; k += 1) {
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
        return dp.get(0).get(true).get(2);
    }
}
