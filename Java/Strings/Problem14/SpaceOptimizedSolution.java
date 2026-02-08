package Strings.Problem14;

import java.util.HashMap;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(nm) and space complexity is O(m).
     */
    public static Integer getMinOps(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Integer> prev = new HashMap<>();
        prev.put(0, 0);
        for (int j = 0; j <= m; j += 1) {
            prev.put(j, j);
        }
        for (int i = 1; i <= n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= m; j += 1) {
                curr.put(j, Integer.MAX_VALUE);
            }
            curr.put(0, i);
            for (int j = 1; j <= m; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    curr.put(j, prev.get(j - 1));
                } else {
                    curr.put(j, Math.min(
                            Math.min(
                                    1 + curr.get(j - 1),
                                    1 + prev.get(j)
                            ),
                            1 + prev.get(j - 1)
                    ));
                }
            }
            prev = curr;
        }
        return prev.get(m);
    }
}
