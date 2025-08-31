package DynamicProgramming.DP11;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n*n*n) and space complexity is O(n + n + n*n).
     */
    public static Integer getMinPathSum(List<List<Integer>> triangle) {
        int n = triangle.size();
        Integer result = Integer.MAX_VALUE;
        for (int j = 0; j < n; j += 1) {
            Map<Integer, Map<Integer, Integer>> dp = getDp(triangle, n);
            result = Math.min(result, solve(triangle, n - 1, j, n, dp));
        }
        return result;
    }

    private static Map<Integer, Map<Integer, Integer>> getDp(List<List<Integer>> triangle, int n) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = 0; j < n; j += 1) {
                row.put(j, null);
            }
            dp.put(i, row);
        }
        return dp;
    }

    private static Integer solve(List<List<Integer>> triangle, int i, int j, int n, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == 0 && j == 0) {
            return triangle.getFirst().getFirst();
        }
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        Integer up = Integer.MAX_VALUE;
        if (0 <= i - 1 && j < i) {
            up = solve(triangle, i - 1, j, n, dp);
        }
        Integer diagonal = Integer.MAX_VALUE;
        if (0 <= i - 1 && 0 <= j - 1) {
            diagonal = solve(triangle, i - 1, j - 1, n, dp);
        }
        dp.get(i).put(j, triangle.get(i).get(j) + Math.min(up, diagonal));
        return dp.get(i).get(j);
    }
}
