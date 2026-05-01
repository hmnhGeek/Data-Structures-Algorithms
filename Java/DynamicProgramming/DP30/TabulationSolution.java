package DynamicProgramming.DP30;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    public static Integer getLcsLength(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j <= m; j += 1) {
                subMap.put(j, 0);
            }
            dp.put(i, subMap);
        }
        for (int i = 1; i <= n; i += 1) {
            for (int j = 1; j <= m; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp.get(i).put(j, 1 + dp.get(i - 1).get(j - 1));
                }
                else {
                    dp.get(i).put(j, Math.max(
                            dp.get(i - 1).get(j),
                            dp.get(i).get(j - 1)
                    ));
                }
            }
        }
        return dp.get(n).get(m);
    }
}
