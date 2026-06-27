package DynamicProgramming.DP34;

import java.util.HashMap;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(nm) and space complexity is O(m).
     */
    public static boolean isMatching(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Boolean> prev = new HashMap<>();
        for (int j = 0; j < m + 1; j += 1) {
            prev.put(j, false);
        }
        prev.put(0, true);
        for (int i = 1; i < n + 1; i += 1) {
            Map<Integer, Boolean> curr = new HashMap<>();
            for (int j = 0; j < m + 1; j += 1) {
                curr.put(j, false);
            }
            boolean setTrue = true;
            for (int k = i - 1; k >= 0; k -= 1) {
                if (s1.charAt(k) != '*') {
                    setTrue = false;
                    break;
                }
            }
            curr.put(0, setTrue);
            for (int j = 1; j < m + 1; j += 1) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1) || s1.charAt(i - 1) == '?') {
                    curr.put(j, prev.get(j - 1));
                } else if (s1.charAt(i - 1) == '*') {
                    curr.put(j, prev.get(j) || curr.get(j - 1));
                } else {
                    curr.put(j, false);
                }
            }
            prev = curr;
        }
        return prev.get(m);
    }
}
