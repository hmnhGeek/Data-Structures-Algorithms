package DynamicProgramming.DP33;

import java.util.HashMap;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(nm) and space complexity is O(m).
     */
    public static Integer getMinOps(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Integer> prev = getPrev(n, m);

        for (int i = 1; i <= n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= m; j += 1) {
                if (j == 0) {
                    curr.put(j, i);
                    continue;
                }
                curr.put(j, 0);
            }
            for (int j = 1; j <= m; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    curr.put(j, prev.get(j - 1));
                } else {
                    curr.put(j, 1 + Math.min(
                            curr.get(j - 1),
                            Math.min(
                                    prev.get(j),
                                    prev.get(j - 1)
                            )
                    ));
                }
            }
            prev = curr;
        }

        return prev.get(m);
    }

    private static Map<Integer, Integer> getPrev(int n, int m) {
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j <= m; j += 1) {
            if (j == 0) {
                prev.put(j, 0);
                continue;
            }
            prev.put(j, j);
        }
        return prev;
    }
}
