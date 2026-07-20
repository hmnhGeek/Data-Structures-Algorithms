package DynamicProgramming.DP37;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    public static Integer findMaxProfit(List<Integer> arr) {
        /*
            Time complexity is O(4n) and space complexity is O(n + 4n).
         */
        int n = arr.size();
        Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Boolean, Map<Integer, Integer>> sub = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                Map<Integer, Integer> sub2 = new HashMap<>();
                for (int k = 0; k <= 2; k += 1) {
                    sub2.put(k, null);
                }
                sub.put(j, sub2);
            }
            dp.put(i, sub);
        }
        return solve(arr, 0, true, 2, n, dp);
    }

    private static Integer solve(List<Integer> arr, int i, boolean j, int k, int n, Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp) {
        if (k == 0) return 0;
        if (i == n) return 0;
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
