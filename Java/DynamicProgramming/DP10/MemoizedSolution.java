package DynamicProgramming.DP10;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(m * n) and space complexity is O(m + n + mn).
     */
    public static Integer minPathSum(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = 0; j < m; j += 1) {
                row.put(j, null);
            }
            dp.put(i, row);
        }
        return solve(mtx, n - 1, m - 1, n, m, dp);
    }

    private static Integer solve(List<List<Integer>> mtx, int i, int j, int n, int m, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == 0 && j == 0) {
            return mtx.getFirst().getFirst();
        }
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        Integer left = Integer.MAX_VALUE;
        if (0 <= i - 1 && i - 1 < n) {
            left = mtx.get(i).get(j) + solve(mtx, i - 1, j, n, m, dp);
        }
        Integer right = Integer.MAX_VALUE;
        if (0 <= j - 1 && j - 1 < m) {
            right = mtx.get(i).get(j) + solve(mtx, i, j - 1, n, m, dp);
        }
        dp.get(i).put(j, Math.min(left, right));
        return dp.get(i).get(j);
    }
}
