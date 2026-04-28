package Strings.Problem17;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class RecursiveSolution {
    /*
        Time complexity is O(n * 2^n) and space complexity is O(n).
     */
    public static boolean wordBreak(String string, List<String> dict) {
        Set<String> dictionary = new HashSet<>(dict);
        int n = string.length();
        return solve(0, string, n, dictionary);
    }

    private static boolean solve(int i, String string, int n, Set<String> dictionary) {
        if (i == n) {
            // you were able to reach the end and thus all previous possible words
            // exist, so return true.
            return true;
        }

        StringBuilder sb = new StringBuilder();
        for (int j = i; j < n; j += 1) {
            sb.append(string.charAt(j));
            if (dictionary.contains(sb.toString()) && solve(j + 1, string, n, dictionary)) {
                return true;
            }
        }
        return false;
    }
}
