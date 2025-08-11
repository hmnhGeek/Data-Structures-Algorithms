package DynamicProgramming.DP9;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer getPathCount(List<List<Integer>> mtx) {
        /*
            Time complexity is O(mn) and space complexity is O(m).
         */
        if (mtx.getFirst().getFirst().equals(-1) || mtx.getLast().getLast().equals(-1)) return 0;
        int n = mtx.size(), m = mtx.getFirst().size();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = -1; j < m; j += 1) {
            prev.put(j, 0);
        }
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = -1; j < m; j += 1) {
                curr.put(j, 0);
            }
            if (i == 0) {
                curr.put(0, 1);
            }
            for (int j = 0; j < m; j += 1) {
                if (i == 0 && j == 0) continue;
                if (mtx.get(i).get(j).equals(-1)) continue;
                Integer upDirection = prev.get(j);
                Integer leftDirection = curr.get(j - 1);
                curr.put(j, upDirection + leftDirection);
            }
            prev = curr;
        }
        return prev.get(m - 1);
    }

    private static Map<Integer, Map<Integer, Integer>> getBlankDp(int n, int m) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = -1; i < n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = -1; j < m; j += 1) {
                row.put(j, 0);
            }
            dp.put(i, row);
        }
        return dp;
    }
}
