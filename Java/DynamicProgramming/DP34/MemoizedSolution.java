package DynamicProgramming.DP34;

import java.util.HashMap;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(nm) and space complexity is O(n + m + nm).
     */
    public static boolean isMatching(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Map<Integer, Boolean>> dp = new HashMap<>();
        for (int i = 0; i < n + 1; i += 1) {
            Map<Integer, Boolean> prev = new HashMap<>();
            for (int j = 0; j < m + 1; j += 1) {
                prev.put(j, null);
            }
            dp.put(i, prev);
        }
        return solve(s1, n, s2, m, dp);
    }

    private static boolean solve(String s1, int i, String s2, int j, Map<Integer, Map<Integer, Boolean>> dp) {
        if (i == 0 && j == 0) return true;
        if (i == 0 && j > 0) return false;
        if (i > 0 && j == 0) {
            for (int k = i - 1; k >= 0; k -= 1) {
                if (s1.charAt(k) != '*') return false;
            }
            return true;
        }
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        if (s1.charAt(i - 1) == s2.charAt(j - 1) || s1.charAt(i - 1) == '?') {
            dp.get(i).put(j, solve(s1, i - 1, s2, j - 1, dp));
        } else if (s1.charAt(i - 1) == '*') {
            dp.get(i).put(j, solve(s1, i - 1, s2, j, dp) || solve(s1, i, s2, j - 1, dp));
        } else {
            dp.get(i).put(j, false);
        }
        return dp.get(i).get(j);
    }
}
