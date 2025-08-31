package DynamicProgramming.DP10;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(m * n) and space complexity is O(mn).
     */
    public static Integer minPathSum(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = 0; j < m; j += 1) {
                row.put(j, Integer.MAX_VALUE);
            }
            dp.put(i, row);
        }
        dp.get(0).put(0, mtx.getFirst().getFirst());
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (i == 0 && j == 0) {
                    continue;
                }
                Integer left = Integer.MAX_VALUE;
                if (0 <= i - 1 && i - 1 < n) {
                    left = mtx.get(i).get(j) + dp.get(i - 1).get(j);
                }
                Integer right = Integer.MAX_VALUE;
                if (0 <= j - 1 && j - 1 < m) {
                    right = mtx.get(i).get(j) + dp.get(i).get(j - 1);
                }
                dp.get(i).put(j, Math.min(left, right));
            }
        }
        return dp.get(n - 1).get(m - 1);
    }
}
