package DynamicProgramming.DP22;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(nk) and space complexity O(nk).
     */
    public static Integer getNumWays(List<Integer> coins, Integer target) {
        if (target < 0) return null;
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < coins.size(); i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int k = 0; k < target + 1; k += 1) {
                prev.put(k, 0);
            }
            dp.put(i, prev);
        }
        for (int i = 0; i < coins.size(); i += 1) {
            dp.get(i).put(0, 1);
        }
        for (int k = 0; k < target + 1; k += 1) {
            if (k % coins.getFirst() == 0) {
                dp.get(0).put(k, 1);
            }
        }
        for (int i = 1; i < coins.size(); i += 1) {
            for (int k = 0; k < target + 1; k += 1) {
                Integer left = 0;
                if (coins.get(i) <= k) {
                    left = dp.get(i).get(k - coins.get(i));
                }
                Integer right = dp.get(i - 1).get(k);
                dp.get(i).put(k, left + right);
            }
        }
        return dp.get(coins.size() - 1).get(target);
    }
}
