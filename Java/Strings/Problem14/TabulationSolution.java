package Strings.Problem14;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(nm) and space complexity is O(nm).
     */
    public static Integer getMinOps(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Integer, Integer> subDp = new HashMap<>();
            for (int j = 0; j <= m; j += 1) {
                subDp.put(j, Integer.MAX_VALUE);
            }
            dp.put(i, subDp);
        }
        for (int j = 0; j <= m; j += 1) {
            dp.get(0).put(j, j);
        }
        for (int i = 0; i <= n; i += 1) {
            dp.get(i).put(0, i);
        }
        for (int i = 1; i <= n; i += 1) {
            for (int j = 1; j <= m; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp.get(i).put(j, dp.get(i - 1).get(j - 1));
                } else {
                    dp.get(i).put(j, Math.min(
                            Math.min(
                                    1 + dp.get(i).get(j - 1),
                                    1 + dp.get(i - 1).get(j)
                            ),
                            1 + dp.get(i - 1).get(j - 1)
                    ));
                }
            }
        }
        return dp.get(n - 1).get(m - 1);
    }
}
