package DynamicProgramming.DP16;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n * target) and space complexity is O(n + n * target).
     */
    public static boolean subsetSum(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Map<Integer, Boolean>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Boolean> subDp = new HashMap<>();
            for (int j = 0; j <= target; j += 1) {
                subDp.put(j, null);
            }
            dp.put(i, subDp);
        }
        return solve(arr, n - 1, target, dp);
    }

    public static boolean solve(List<Integer> arr, int i, int j, Map<Integer, Map<Integer, Boolean>> dp) {
        if (j == 0) return true;
        if (i == 0) {
            return arr.getFirst() == j;
        }
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        boolean left = false;
        if (arr.get(i) <= j) {
            left = solve(arr, i - 1, j - arr.get(i), dp);
        }
        boolean right = solve(arr, i - 1, j, dp);
        dp.get(i).put(j, left || right);
        return dp.get(i).get(j);
    }
}
