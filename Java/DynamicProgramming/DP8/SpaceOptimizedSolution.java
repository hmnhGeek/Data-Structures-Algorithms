package DynamicProgramming.DP8;

import java.util.HashMap;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer getUniquePathsCount(Integer n, Integer m) {
        /*
            Time complexity is O(m * n) and space complexity is O(m).
         */
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = -1; j < m; j += 1) {
            prev.put(j, 0);
        }

        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = -1; j < m; j += 1) {
                curr.put(j, 0);
            }
            if (i == 0) curr.put(0, 1);
            for (int j = 0; j < m; j += 1) {
                if (i == 0 && j == 0) continue;
                Integer upDirection = prev.get(j);
                Integer leftDirection = curr.get(j - 1);
                curr.put(j, upDirection + leftDirection);
            }
            prev = curr;
        }
        return prev.get(m - 1);
    }
}
