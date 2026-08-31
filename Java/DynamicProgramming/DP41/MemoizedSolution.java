package DynamicProgramming.DP41;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n + n^2).
     */
    public static Integer getLISLength(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j <= n + 1; j += 1) {
                prev.put(j, null);
            }
            dp.put(i, prev);
        }
        return solve(arr, n - 1, n, n, dp);
    }

    private static Integer solve(List<Integer> arr, int i, int j, int n, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == 0) {
            if (arr.get(i) < Utils.getValAtIdx(arr, j, n)) {
                return 1;
            }
            return 0;
        }
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        Integer left = Integer.MIN_VALUE;
        if (arr.get(i) < Utils.getValAtIdx(arr, j, n)) {
            left = 1 + solve(arr, i - 1, i, n, dp);
        }
        Integer right = solve(arr, i - 1, j, n, dp);
        dp.get(i).put(j, Math.max(left, right));
        return dp.get(i).get(j);
    }
}
