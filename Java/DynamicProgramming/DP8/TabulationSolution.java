package DynamicProgramming.DP8;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    public static Integer getUniquePathsCount(Integer n, Integer m) {
        /*
            Time complexity is O(m * n) and space complexity is O(m * n).
         */
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = -1; i < n; i += 1) {
            Map<Integer, Integer> mp = new HashMap<>();
            for (int j = -1; j < m; j += 1) {
                mp.put(j, 0);
            }
            dp.put(i, mp);
        }
        dp.get(0).put(0, 1);

        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (i == 0 && j == 0) continue;
                Integer upDirection = dp.get(i - 1).get(j);
                Integer leftDirection = dp.get(i).get(j - 1);
                dp.get(i).put(j, upDirection + leftDirection);
            }
        }
        return dp.get(n - 1).get(m - 1);
    }
}
