package DynamicProgramming.DP11;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n*n*n) and space complexity is O(n*n).
     */
    public static Integer getMinPathSum(List<List<Integer>> triangle) {
        int n = triangle.size();
        Integer result = Integer.MAX_VALUE;
        for (int k = 0; k < n; k += 1) {
            Map<Integer, Map<Integer, Integer>> dp = getDp(triangle, n);

            for (int i = 1; i < n; i += 1) {
                for (int j = 0; j < i + 1; j += 1) {
                    Integer up = Integer.MAX_VALUE;
                    if (0 <= i - 1 && j < i) {
                        up = dp.get(i - 1).get(j);
                    }
                    Integer diagonal = Integer.MAX_VALUE;
                    if (0 <= i - 1 && 0 <= j - 1) {
                        diagonal = dp.get(i - 1).get(j - 1);
                    }
                    dp.get(i).put(j, triangle.get(i).get(j) + Math.min(up, diagonal));
                }
            }

            result = Math.min(result, dp.get(n - 1).get(k));
        }
        return result;
    }

    private static Map<Integer, Map<Integer, Integer>> getDp(List<List<Integer>> triangle, int n) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = 0; j < n; j += 1) {
                row.put(j, Integer.MAX_VALUE);
            }
            dp.put(i, row);
        }
        dp.get(0).put(0, triangle.getFirst().getFirst());
        return dp;
    }
}
