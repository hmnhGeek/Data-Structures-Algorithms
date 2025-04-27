package DynamicProgramming.DP54;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    private static Integer solve(List<Integer> arr, Integer i, Integer k, Integer n, Map<Integer, Integer> dp) {
        if (i.equals(n)) return 0;
        if (dp.get(i) != null) return dp.get(i);
        Integer maxCost = Integer.MIN_VALUE;
        Integer maxValue = Integer.MIN_VALUE;
        for (int j = i; j < Math.min(i + k, n); j += 1) {
            maxValue = Math.max(arr.get(j), maxValue);
            Integer cost = (maxValue * (j - i + 1)) + solve(arr, j + 1, k, n, dp);
            maxCost = Math.max(maxCost, cost);
        }
        dp.put(i, maxCost);
        return dp.get(i);
    }

    public static Integer maxSumPartition(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(n*k) and space complexity is O(n + n).
         */
        int n = arr.size();
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            dp.put(i, null);
        }
        return solve(arr, 0, k, n, dp);
    }
}