package DynamicProgramming.DP54;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    public static Integer maxSumPartition(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(n*k) and space complexity is O(n).
         */
        int n = arr.size();
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            dp.put(i, Integer.MIN_VALUE);
        }
        dp.put(n, 0);

        for (int i = n - 1; i >= 0; i -= 1) {
            Integer maxCost = Integer.MIN_VALUE;
            Integer maxValue = Integer.MIN_VALUE;
            for (int j = i; j < Math.min(i + k, n); j += 1) {
                maxValue = Math.max(arr.get(j), maxValue);
                Integer cost = (maxValue * (j - i + 1)) + dp.get(j + 1);
                maxCost = Math.max(maxCost, cost);
            }
            dp.put(i, maxCost);
        }

        return dp.get(0);
    }
}