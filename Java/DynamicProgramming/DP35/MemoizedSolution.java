package DynamicProgramming.DP35;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n) and space complexity is O(n + n)
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Boolean, Map<Integer, Integer>> prev = new HashMap<>();
            for (Boolean bool : Arrays.asList(true, false)) {
                Map<Integer, Integer> subMap = new HashMap<>();
                subMap.put(0, null);
                subMap.put(1, null);
                prev.put(bool, subMap);
            }
            dp.put(i, prev);
        }
        return solve(arr, 0, true, 1, n, dp);
    }

    private static Integer solve(List<Integer> arr, int i, boolean canBuy, int j, int n, Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp) {
        if (j <= 0) return 0;
        if (i >= n) return 0;
        if (dp.get(i).get(canBuy).get(j) != null) {
            return dp.get(i).get(canBuy).get(j);
        }
        if (canBuy) {
            dp.get(i).get(canBuy).put(j, Math.max(
                    -arr.get(i) + solve(arr, i + 1, false, j, n, dp),
                    solve(arr, i + 1, true, j, n, dp)
            ));
        } else {
            dp.get(i).get(canBuy).put(j, Math.max(
                    arr.get(i) + solve(arr, i + 1, true, j - 1, n, dp),
                    solve(arr, i + 1, false, j, n, dp)
            ));
        }
        return dp.get(i).get(canBuy).get(j);
    }
}
