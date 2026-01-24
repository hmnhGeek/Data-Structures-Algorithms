package DynamicProgramming.DP22;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(nk) and space complexity O(k).
     */
    public static Integer getNumWays(List<Integer> coins, Integer target) {
        if (target < 0) return null;
        Map<Integer, Integer> prev = new HashMap<>();
        for (int k = 0; k < target + 1; k += 1) {
            prev.put(k, 0);
        }
        prev.put(0, 1);
        for (int k = 0; k < target + 1; k += 1) {
            if (k % coins.getFirst() == 0) {
                prev.put(k, 1);
            }
        }
        for (int i = 1; i < coins.size(); i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int k = 0; k < target + 1; k += 1) {
                curr.put(k, 0);
            }
            curr.put(0, 1);
            for (int k = 0; k < target + 1; k += 1) {
                Integer left = 0;
                if (coins.get(i) <= k) {
                    left = curr.get(k - coins.get(i));
                }
                Integer right = prev.get(k);
                curr.put(k, left + right);
            }
            prev = curr;
        }
        return prev.get(target);
    }
}
