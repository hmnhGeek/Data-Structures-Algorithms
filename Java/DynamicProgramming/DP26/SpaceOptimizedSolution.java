package DynamicProgramming.DP26;

import java.util.HashMap;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer getLcsLength(String s1, String s2) {
        int n1 = s1.length(), n2 = s2.length();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j <= n2; j += 1) {
            prev.put(j, 0);
        }
        for (int i = 1; i <= n1; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= n2; j += 1) {
                curr.put(j, 0);
            }
            for (int j = 1; j <= n2; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    curr.put(j, 1 + prev.get(j - 1));
                } else {
                    curr.put(j, Math.max(
                            prev.get(j),
                            curr.get(j - 1)
                    ));
                }
            }
            prev = curr;
        }
        return prev.get(n2);
    }
}
