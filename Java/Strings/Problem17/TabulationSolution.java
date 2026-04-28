package Strings.Problem17;

import java.util.*;

public class TabulationSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n).
     */
    public static boolean wordBreak(String string, List<String> dict) {
        Set<String> dictionary = new HashSet<>(dict);
        int n = string.length();
        Map<Integer, Boolean> dp = new HashMap<>();
        for (int i = 0; i < n + 1; i += 1) {
            dp.put(i, false);
        }
        dp.put(n, true);
        for (int i = n - 1; i >= 0; i -= 1)  {
            StringBuilder sb = new StringBuilder();
            for (int j = i; j < n; j += 1) {
                sb.append(string.charAt(j));
                if (dictionary.contains(sb.toString()) && dp.get(j + 1)) {
                    dp.put(i, true);
                    break;
                }
            }
        }
        return dp.get(0);
    }
}
