package Strings.Problem14;

import java.util.HashMap;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(nm) and space complexity is O(n + m + nm).
     */
    public static Integer getMinOps(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Integer, Integer> subDp = new HashMap<>();
            for (int j = 0; j <= m; j += 1) {
                subDp.put(j, null);
            }
            dp.put(i, subDp);
        }
        return solve(s1, n - 1, s2, m - 1, dp);
    }

    public static Integer solve(String s1, int i, String s2, int j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == 0) return j;
        if (j == 0) return i;
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
            dp.get(i).put(j, solve(s1, i - 1, s2, j - 1, dp));
        } else {
            dp.get(i).put(j, Math.min(
                    Math.min(
                            1 + solve(s1, i, s2, j - 1, dp),
                            1 + solve(s1, i - 1, s2, j, dp)
                    ),
                    1 + solve(s1, i - 1, s2, j - 1, dp)
            ));
        }
        return dp.get(i).get(j);
    }
}
