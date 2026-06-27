package DynamicProgramming.DP35;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n) and space complexity is O(1)
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        Map<Boolean, Map<Integer, Integer>> next = new HashMap<>();
        for (Boolean bool : Arrays.asList(true, false)) {
            Map<Integer, Integer> subMap = new HashMap<>();
            subMap.put(0, 0);
            subMap.put(1, 0);
            next.put(bool, subMap);
        }

        for (int i = n - 1; i >= 0; i -= 1) {
            Map<Boolean, Map<Integer, Integer>> curr = new HashMap<>();
            for (Boolean bool : Arrays.asList(true, false)) {
                Map<Integer, Integer> subMap = new HashMap<>();
                subMap.put(0, 0);
                subMap.put(1, 0);
                curr.put(bool, subMap);
            }
            for (Boolean canBuy : Arrays.asList(true, false)) {
                for (int j = 1; j >= 0; j--) {

                    if (j == 0) {
                        curr.get(true).put(0, 0);
                        curr.get(false).put(0, 0);
                        continue;
                    }

                    if (canBuy) {
                        curr.get(true).put(j,
                                Math.max(
                                        -arr.get(i) + next.get(false).get(j),
                                        next.get(true).get(j)
                                )
                        );
                    } else {
                        curr.get(false).put(j,
                                Math.max(
                                        arr.get(i) + next.get(true).get(j - 1),
                                        next.get(false).get(j)
                                )
                        );
                    }
                }
            }
            next = curr;
        }

        return next.get(true).get(1);
    }
}
