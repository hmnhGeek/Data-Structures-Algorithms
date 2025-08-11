package DynamicProgramming.DP9;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    public static Integer getPathCount(List<List<Integer>> mtx) {
        if (mtx.getFirst().getFirst().equals(-1) || mtx.getLast().getLast().equals(-1)) return 0;
        int n = mtx.size(), m = mtx.getFirst().size();
        Map<Integer, Map<Integer, Integer>> dp = getBlankDp(n, m);
        return solve(mtx, n - 1, m - 1, dp);
    }

    private static Map<Integer, Map<Integer, Integer>> getBlankDp(int n, int m) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = 0; j < m; j += 1) {
                row.put(j, null);
            }
            dp.put(i, row);
        }
        return dp;
    }

    private static Integer solve(List<List<Integer>> mtx, int i, int j, Map<Integer, Map<Integer, Integer>> dp) {
        /*
            Time complexity is O(mn) and space complexity is O(m + n + mn).
         */
        if (i < 0 || j < 0) return 0;
        if (i == 0 && j == 0) return 1;
        if (mtx.get(i).get(j).equals(-1)) return 0;
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        Integer upDirection = solve(mtx, i - 1, j, dp);
        Integer leftDirection = solve(mtx, i, j - 1, dp);
        dp.get(i).put(j, upDirection + leftDirection);
        return dp.get(i).get(j);
    }
}
