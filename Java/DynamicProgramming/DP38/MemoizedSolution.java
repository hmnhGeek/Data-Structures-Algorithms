package DynamicProgramming.DP38;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n * k) and space complexity is O(n + nk).
     */
    public static Integer getMaxProfit(List<Integer> arr, Integer k) {
        int n = arr.size();
        Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Boolean, Map<Integer, Integer>> subMap1 = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                Map<Integer, Integer> subMap2 = new HashMap<>();
                for (int p = 0; p <= k; p += 1) {
                    subMap2.put(p, null);
                }
                subMap1.put(j, subMap2);
            }
            dp.put(i, subMap1);
        }
        return solve(arr, 0, true, k, n, dp);
    }

    private static Integer solve(List<Integer> arr, int i, boolean j, int k, int n, Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp) {
        if (i >= n) return 0;
        if (k == 0) return 0;
        if (dp.get(i).get(j).get(k) != null) return dp.get(i).get(j).get(k);
        if (j) {
            dp.get(i).get(j).put(k, Math.max(
                    -arr.get(i) + solve(arr, i + 1, !j, k, n, dp),
                    solve(arr, i + 1, j, k, n, dp)
            ));
        } else {
            dp.get(i).get(j).put(k, Math.max(
                    arr.get(i) + solve(arr, i + 1, !j, k - 1, n, dp),
                    solve(arr, i + 1, j, k, n, dp)
            ));
        }
        return dp.get(i).get(j).get(k);
    }
}
