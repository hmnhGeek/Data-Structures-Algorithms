package DynamicProgramming.DP21;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(n + n * target).
     */
    public static Integer countSubsets(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j <= target; j += 1) {
                prev.put(j, null);
            }
            dp.put(i, prev);
        }
        return solve(arr, n - 1, target, dp);
    }

    public static Integer solve(List<Integer> arr, int i, int j, Map<Integer, Map<Integer, Integer>> dp) {
        if (j == 0) return 1;
        if (i == 0) {
            if (arr.getFirst() == j) return 1;
            return 0;
        }
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        Integer left = 0;
        if (arr.get(i) <= j) {
            left = solve(arr, i - 1, j - arr.get(i), dp);
        }
        Integer right = solve(arr, i - 1, j, dp);
        dp.get(i).put(j, left + right);
        return dp.get(i).get(j);
    }
}
