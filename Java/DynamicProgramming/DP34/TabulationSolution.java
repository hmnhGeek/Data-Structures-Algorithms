package DynamicProgramming.DP34;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(nm) and space complexity is O(nm).
     */
    public static boolean isMatching(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Map<Integer, Boolean>> dp = new HashMap<>();
        for (int i = 0; i < n + 1; i += 1) {
            Map<Integer, Boolean> prev = new HashMap<>();
            for (int j = 0; j < m + 1; j += 1) {
                prev.put(j, false);
            }
            dp.put(i, prev);
        }
        dp.get(0).put(0, true);
        for (int i = 1; i < n + 1; i += 1) {
            boolean setTrue = true;
            for (int k = i - 1; k >= 0; k -= 1) {
                if (s1.charAt(k) != '*') {
                    setTrue = false;
                    break;
                }
            }
            dp.get(i).put(0, setTrue);
        }
        for (int i = 1; i < n + 1; i += 1) {
            for (int j = 1; j < m + 1; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1) || s1.charAt(i - 1) == '?') {
                    dp.get(i).put(j, dp.get(i - 1).get(j - 1));
                } else if (s1.charAt(i - 1) == '*') {
                    dp.get(i).put(j, dp.get(i - 1).get(j) || dp.get(i).get(j - 1));
                } else {
                    dp.get(i).put(j, false);
                }
            }
        }
        return dp.get(n).get(m);
    }
}
