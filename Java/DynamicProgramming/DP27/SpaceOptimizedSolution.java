package DynamicProgramming.DP27;

import java.util.HashMap;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer getLongestCommonSubstringLength(String s1, String s2) {
        /*
            Time complexity is O(nm) and space complexity is O(m).
         */
        int n = s1.length(), m = s2.length();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j <= m; j += 1) {
            prev.put(j, 0);
        }
        int result = 0;
        for (int i = 1; i <= n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= m; j += 1) {
                curr.put(j, 0);
            }
            for (int j = 1; j <= m; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    curr.put(j, prev.get(j - 1) + 1);
                    result = Math.max(result, curr.get(j));
                }
            }
            prev = curr;
        }
        return result;
    }
}
