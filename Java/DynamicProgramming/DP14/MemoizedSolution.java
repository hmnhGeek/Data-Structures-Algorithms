package DynamicProgramming.DP14;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(nk) and space complexity is O(n + nk).
     */
    public static boolean subsetSum(List<Integer> arr, Integer k) {
        int n = arr.size();
        Map<Integer, Map<Integer, Boolean>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Boolean> sub = new HashMap<>();
            for (int j = 0; j <= k; j += 1) {
                sub.put(j, null);
            }
            dp.put(i, sub);
        }
        return solve(arr, n - 1, k, dp);
    }

    public static boolean solve(List<Integer> arr, int i, int k, Map<Integer, Map<Integer, Boolean>> dp) {
        if (k == 0) return true;
        if (i == 0) {
            if (arr.getFirst() == k) return true;
            return false;
        }
        if (dp.get(i).get(k) != null) return dp.get(i).get(k);
        boolean left = false;
        if (arr.get(i) <= k) {
            left = solve(arr, i - 1, k - arr.get(i), dp);
        }
        boolean right = solve(arr, i - 1, k, dp);
        dp.get(i).put(k, left || right);
        return dp.get(i).get(k);
    }
}
