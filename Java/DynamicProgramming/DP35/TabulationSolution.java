package DynamicProgramming.DP35;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n) and space complexity is O(n)
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Boolean, Map<Integer, Integer>> prev = new HashMap<>();
            for (Boolean bool : Arrays.asList(true, false)) {
                Map<Integer, Integer> subMap = new HashMap<>();
                subMap.put(0, 0);
                subMap.put(1, 0);
                prev.put(bool, subMap);
            }
            dp.put(i, prev);
        }

        for (int i = n - 1; i >= 0; i -= 1) {
            for (Boolean canBuy : Arrays.asList(true, false)) {
                for (int j = 1; j >= 0; j--) {

                    if (j == 0) {
                        dp.get(i).get(true).put(0, 0);
                        dp.get(i).get(false).put(0, 0);
                        continue;
                    }

                    if (canBuy) {
                        dp.get(i).get(true).put(j,
                                Math.max(
                                        -arr.get(i) + dp.get(i + 1).get(false).get(j),
                                        dp.get(i + 1).get(true).get(j)
                                )
                        );
                    } else {
                        dp.get(i).get(false).put(j,
                                Math.max(
                                        arr.get(i) + dp.get(i + 1).get(true).get(j - 1),
                                        dp.get(i + 1).get(false).get(j)
                                )
                        );
                    }
                }
            }
        }

        return dp.get(0).get(true).get(1);
    }
}
