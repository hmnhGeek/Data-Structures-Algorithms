package DynamicProgramming.DP9;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    public static Integer getPathCount(List<List<Integer>> mtx) {
        if (mtx.getFirst().getFirst().equals(-1) || mtx.getLast().getLast().equals(-1)) return 0;
        int n = mtx.size(), m = mtx.getFirst().size();
        Map<Integer, Map<Integer, Integer>> dp = getBlankDp(n, m);
        dp.get(0).put(0, 1);
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (i == 0 && j == 0) continue;
                if (mtx.get(i).get(j).equals(-1)) continue;
                Integer upDirection = dp.get(i - 1).get(j);
                Integer leftDirection = dp.get(i).get(j - 1);
                dp.get(i).put(j, upDirection + leftDirection);
            }
        }
        return dp.get(n - 1).get(m - 1);
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
