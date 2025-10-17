package DynamicProgramming.DP15;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
    Time complexity is O(nk) and space complexity is O(nk + k).
 */
    public static boolean subsetSum(List<Integer> arr) {
        int n = arr.size();
        int k = arr.stream().mapToInt(Integer::intValue).sum();
        if (k % 2 != 0) return false;
        Map<Integer, Map<Integer, Boolean>> dp = new HashMap<>();
        updateDpArray(dp, n, k);
        return solve(arr, n - 1, k / 2, dp);
    }

    private static void updateDpArray(Map<Integer, Map<Integer, Boolean>> dp, int n, int k) {
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Boolean> subMap = new HashMap<>();
            for (int j = 0; j < k; j += 1) {
                subMap.put(j, null);
            }
            dp.put(i, subMap);
        }
    }

    private static boolean solve(List<Integer> arr, int i, Integer k, Map<Integer, Map<Integer, Boolean>> dp) {
        if (k == 0) return true;
        if (i == 0) return arr.getFirst() == k;
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
