package DynamicProgramming.DP32;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(nm) and space complexity is O(n + m).
     */
    public static Integer getDistinctSubsequencesCount(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j <= m; j += 1) {
                if (j == 0) {
                    prev.put(j, 1);
                    continue;
                }
                prev.put(j, 0);
            }
            dp.put(i, prev);
        }

        for (int i = 1; i <= n; i += 1) {
            for (int j = 1; j <= m; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp.get(i).put(j, dp.get(i - 1).get(j - 1) + dp.get(i - 1).get(j));
                } else {
                    dp.get(i).put(j, dp.get(i - 1).get(j));
                }
            }
        }
        return dp.get(n).get(m);
    }
}
