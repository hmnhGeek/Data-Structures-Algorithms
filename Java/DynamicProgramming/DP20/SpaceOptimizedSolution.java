package DynamicProgramming.DP20;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(target).
     */
    public static Integer getMinCoins(List<Integer> denominations, Integer target) {
        int n = denominations.size();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j <= target; j += 1) {
            prev.put(j, Integer.MAX_VALUE);
        }
        prev.put(0, 0);
        for (int j = 0; j <= target; j += 1) {
            if (j % denominations.getFirst() == 0) {
                prev.put(j, j / denominations.getFirst());
            }
        }

        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= target; j += 1) {
                curr.put(j, Integer.MAX_VALUE);
            }
            curr.put(0, 0);
            for (int j = 0; j <= target; j += 1) {
                Integer left = Integer.MAX_VALUE;
                if (j >= denominations.get(i)) {
                    Integer subCoinsCount = curr.get(j - denominations.get(i));
                    if (subCoinsCount != Integer.MAX_VALUE) {
                        left = 1 + subCoinsCount;
                    }
                }
                Integer right = prev.get(j);
                curr.put(j, Math.min(left, right));
            }
            prev = curr;
        }

        Integer count = prev.get(target);
        if (count == Integer.MAX_VALUE) return -1;
        return count;
    }
}
