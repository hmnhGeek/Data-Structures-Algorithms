package PracticeSet1.DynamicProgramming.DP48;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n^3) and space complexity is O(n + n^2).
     */
    public static Integer getMinCostForMultiplication(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j < n; j += 1) {
                subMap.put(j, null);
            }
            dp.put(i, subMap);
        }
        return solve(arr, 1, n - 1, dp);
    }

    private static Integer solve(List<Integer> arr, int i, int j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == j) {
            return 0;
        }
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        Integer minOps = Integer.MAX_VALUE;
        for (int k = i; k < j; k += 1) {
            Integer operations = (arr.get(i - 1) * arr.get(k) * arr.get(j)) + solve(arr, i, k, dp) + solve(arr, k + 1, j, dp);
            minOps = Math.min(minOps, operations);
        }
        dp.get(i).put(j, minOps);
        return dp.get(i).get(j);
    }
}
