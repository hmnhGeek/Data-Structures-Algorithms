package Strings.Problem17;

import java.util.*;

public class MemoizedSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n + n).
     */
    public static boolean wordBreak(String string, List<String> dict) {
        Set<String> dictionary = new HashSet<>(dict);
        int n = string.length();
        Map<Integer, Boolean> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            dp.put(i, null);
        }
        return solve(0, string, n, dictionary, dp);
    }

    private static boolean solve(int i, String string, int n, Set<String> dictionary, Map<Integer, Boolean> dp) {
        if (i == n) {
            // you were able to reach the end and thus all previous possible words
            // exist, so return true.
            return true;
        }
        if (dp.get(i) != null) return dp.get(i);
        StringBuilder sb = new StringBuilder();
        for (int j = i; j < n; j += 1) {
            sb.append(string.charAt(j));
            if (dictionary.contains(sb.toString()) && solve(j + 1, string, n, dictionary, dp)) {
                dp.put(i, true);
                return dp.get(i);
            }
        }
        dp.put(i, false);
        return dp.get(i);
    }
}
