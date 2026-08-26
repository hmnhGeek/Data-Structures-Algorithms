package Strings.Problem22;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n^2).
     */
    public static Integer countPalindromicSubsequences(String string) {
        int n = string.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = n - 1; j >= 0; j -= 1) {
                subMap.put(j, 0);
            }
            dp.put(i, subMap);
        }
        for (int i = 0; i < n; i += 1) {
            dp.get(i).put(i, 1);
        }
        for (int i = n - 2; i >= 0; i -= 1) {
            for (int j = i + 1; j < n; j += 1) {
                if (string.charAt(i) == string.charAt(j)) {
                    dp.get(i).put(j, 1 + dp.get(i + 1).get(j) + dp.get(i).get(j - 1));
                } else {
                    dp.get(i).put(j, dp.get(i + 1).get(j) + dp.get(i).get(j - 1) - dp.get(i + 1).get(j - 1));
                }
            }
        }
        return dp.get(0).get(n - 1);
    }
}
