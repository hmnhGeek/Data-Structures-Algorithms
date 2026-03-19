package DynamicProgramming.DP27;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    public static Integer getLongestCommonSubstringLength(String s1, String s2) {
        /*
            Time complexity is O(nm) and space complexity is O(nm).
         */
        int n = s1.length(), m = s2.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        updateDefaultDP(dp, n, m);
        int result = 0;
        for (int i = 1; i <= n; i += 1) {
            for (int j = 1; j <= m; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp.get(i).put(j, dp.get(i - 1).get(j - 1) + 1);
                    result = Math.max(result, dp.get(i).get(j));
                }
            }
        }
        return result;
    }

    private static void updateDefaultDP(Map<Integer, Map<Integer, Integer>> dp, int n, int m) {
        for (int i = 0; i <= n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = 0; j <= m; j += 1) {
                row.put(j, 0);
            }
            dp.put(i, row);
        }
    }
}
