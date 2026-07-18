package DynamicProgramming.DP36;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n) and space complexity is O(2n).
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Map<Boolean, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Boolean, Integer> subMap = new HashMap<>();
            subMap.put(true, null);
            subMap.put(false, null);
            dp.put(i, subMap);
        }
        return solve(arr, 0, true, n, dp);
    }

    private static Integer solve(List<Integer> arr, int i, boolean j, int n, Map<Integer, Map<Boolean, Integer>> dp) {
        if (i == n) return 0;
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        if (j) {
            dp.get(i).put(j, Math.max(
                    -arr.get(i) + solve(arr, i + 1, !j, n, dp),
                    solve(arr, i + 1, j, n, dp)
            ));
        } else {
            dp.get(i).put(j, Math.max(
                    arr.get(i) + solve(arr, i + 1, !j, n, dp),
                    solve(arr, i + 1, j, n, dp)
            ));
        }
        return dp.get(i).get(j);
    }
}
