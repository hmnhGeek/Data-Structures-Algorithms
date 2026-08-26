package Strings.Problem22;

import java.util.HashMap;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n).
     */
    public static Integer countPalindromicSubsequences(String string) {
        int n = string.length();

        // this is for i = n - 1
        Map<Integer, Integer> nxt = new HashMap<>();
        for (int j = n - 1; j >= 0; j -= 1) {
            nxt.put(j, 0);
        }
        nxt.put(n - 1, 1);
        for (int i = n - 2; i >= 0; i -= 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = n - 1; j >= 0; j -= 1) {
                curr.put(j, 0);
            }
            curr.put(i, 1);
            for (int j = i + 1; j < n; j += 1) {
                if (string.charAt(i) == string.charAt(j)) {
                    curr.put(j, 1 + nxt.get(j) + curr.get(j - 1));
                } else {
                    curr.put(j, nxt.get(j) + curr.get(j - 1) - nxt.get(j - 1));
                }
            }
            nxt = curr;
        }
        return nxt.get(n - 1);
    }
}
