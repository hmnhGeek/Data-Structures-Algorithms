package DynamicProgramming.DP31;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String getShortestCommonSuperSequence(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j <= m; j += 1) {
                prev.put(j, 0);
            }
            dp.put(i, prev);
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
        StringBuilder sb = new StringBuilder();
        int i = n, j = m;
        while (i > 0 && j > 0) {
            if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                sb.append(s1.charAt(i - 1));
                i -= 1;
                j -= 1;
            } else if (dp.get(i - 1).get(j) > dp.get(i).get(j - 1)) {
                sb.append(s1.charAt(i - 1));
                i -= 1;
            } else {
                sb.append(s2.charAt(j - 1));
                j -= 1;
            }
        }
        while (i > 0) {
            sb.append(s1.charAt(i - 1));
            i -= 1;
        }
        while (j > 0) {
            sb.append(s2.charAt(j - 1));
            j -= 1;
        }
        StringBuilder finalSb = sb.reverse();
        return finalSb.toString();
    }

    public static void main(String[] args) {
        System.out.println(Solution.getShortestCommonSuperSequence("brute", "groot"));
        System.out.println(Solution.getShortestCommonSuperSequence("bleed", "blue"));
        System.out.println(Solution.getShortestCommonSuperSequence("coding", "ninjas"));
        System.out.println(Solution.getShortestCommonSuperSequence("blinding", "lights"));
    }
}
