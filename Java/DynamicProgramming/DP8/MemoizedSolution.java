package DynamicProgramming.DP8;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    public static Integer getUniquePathsCount(Integer n, Integer m) {
        /*
            Time complexity is O(m * n) and space complexity is O(n + m + m*n).
         */
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> mp = new HashMap<>();
            for (int j = 0; j < m; j += 1) {
                mp.put(j, null);
            }
            dp.put(i, mp);
        }
        return solve(n - 1, m - 1, dp);
    }

    private static Integer solve(Integer i, Integer j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i < 0 || j < 0) return 0;
        if (i.equals(0) && j.equals(0)) return 1;
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        Integer upDirection = solve(i - 1, j, dp);
        Integer leftDirection = solve(i, j - 1, dp);
        dp.get(i).put(j, upDirection + leftDirection);
        return dp.get(i).get(j);
    }
}
