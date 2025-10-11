package Strings.Problem7;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    public static Integer findLcs(String s1, String s2) {
        /*
            Time complexity is O(mn) and space complexity is O(nm).
         */
        int n1 = s1.length(), n2 = s2.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        populateBlankDp(n1, n2, dp);

        for (int i = 0; i < n1; i += 1) {
            for (int j = 0; j < n2; j += 1) {
                if (s1.charAt(i) == s2.charAt(j)) {
                    dp.get(i).put(j, 1 + dp.get(i - 1).get(j - 1));
                } else {
                    dp.get(i).put(j, Math.max(dp.get(i - 1).get(j), dp.get(i).get(j - 1)));
                }
            }
        }

        return dp.get(n1 - 1).get(n2 - 1);
    }

    private static void populateBlankDp(int n1, int n2, Map<Integer, Map<Integer, Integer>> dp) {
        for (int i = -1; i < n1; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = -1; j < n2; j += 1) {
                subMap.put(j, 0);
            }
            dp.put(i, subMap);
        }
    }
}
