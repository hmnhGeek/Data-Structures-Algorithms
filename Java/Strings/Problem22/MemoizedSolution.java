package Strings.Problem22;

import java.util.HashMap;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n + n^2).
     */
    public static Integer countPalindromicSubsequences(String string) {
        int n = string.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = n; j >= 0; j -= 1) {
                subMap.put(j, null);
            }
            dp.put(i, subMap);
        }
        return solve(string, 0, n - 1, dp);
    }

    private static Integer solve(String string, int i, int j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i > j) return 0;
        if (i == j) return 1;
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        if (string.charAt(i) == string.charAt(j)) {
            dp.get(i).put(j, 1 + solve(string, i + 1, j, dp) + solve(string, i, j - 1, dp));
        } else {
            dp.get(i).put(j, solve(string, i + 1, j, dp) + solve(string, i, j - 1, dp) - solve(string, i + 1, j - 1, dp));
        }
        return dp.get(i).get(j);
    }
}
