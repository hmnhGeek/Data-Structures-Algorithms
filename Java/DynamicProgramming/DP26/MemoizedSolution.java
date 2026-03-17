package DynamicProgramming.DP26;

import java.util.HashMap;
import java.util.Map;

public class MemoizedSolution {
    public static Integer getLcsLength(String s1, String s2) {
        int n1 = s1.length(), n2 = s2.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n1; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j <= n2; j += 1) {
                prev.put(j, null);
            }
            dp.put(i, prev);
        }
        return solve(s1, n1, s2, n2, dp);
    }

    private static Integer solve(String s1, int i, String s2, int j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == 0 || j == 0) return 0;
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
            dp.get(i).put(j, 1 + solve(s1, i - 1, s2, j - 1, dp));
        } else {
            dp.get(i).put(j, Math.max(
                    solve(s1, i - 1, s2, j, dp),
                    solve(s1, i, s2, j - 1, dp)
            ));
        }
        return dp.get(i).get(j);
    }
}
