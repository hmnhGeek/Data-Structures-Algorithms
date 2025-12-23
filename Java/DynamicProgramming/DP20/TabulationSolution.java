package DynamicProgramming.DP20;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(n * target).
     */
    public static Integer getMinCoins(List<Integer> denominations, Integer target) {
        int n = denominations.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> subDp = new HashMap<>();
            for (int j = 0; j <= target; j += 1) {
                subDp.put(j, Integer.MAX_VALUE);
            }
            dp.put(i, subDp);
        }
        for (int i = 0; i < n; i += 1) {
            dp.get(i).put(0, 0);
        }
        for (int j = 0; j <= target; j += 1) {
            if (j % denominations.getFirst() == 0) {
                dp.get(0).put(j, j / denominations.getFirst());
            }
        }

        for (int i = 1; i < n; i += 1) {
            for (int j = 0; j <= target; j += 1) {
                Integer left = Integer.MAX_VALUE;
                if (j >= denominations.get(i)) {
                    Integer subCoinsCount = dp.get(i).get(j - denominations.get(i));
                    if (subCoinsCount != Integer.MAX_VALUE) {
                        left = 1 + subCoinsCount;
                    }
                }
                Integer right = dp.get(i - 1).get(j);
                dp.get(i).put(j, Math.min(left, right));
            }
        }

        Integer count = dp.get(n - 1).get(target);
        if (count == Integer.MAX_VALUE) return -1;
        return count;
    }
}
