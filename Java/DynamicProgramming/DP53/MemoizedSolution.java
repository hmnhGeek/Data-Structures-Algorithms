package DynamicProgramming.DP53;

import java.util.HashMap;
import java.util.Map;

public class MemoizedSolution {
    private static Integer solve(String string, Integer i, Integer n, Map<Integer, Integer> dp) {
        if (i.equals(n)) return 0;
        if (dp.get(i) != null) return dp.get(i);
        Integer minimumPartitions = Integer.MAX_VALUE;
        StringBuilder temp = new StringBuilder();
        for (int j = i; j < n; j += 1) {
            temp.append(string.charAt(j));
            if (PalindromeChecker.isPalindrome(String.valueOf(temp))) {
                Integer partitions = 1 + solve(string, j + 1, n, dp);
                minimumPartitions = Math.min(minimumPartitions, partitions);
            }
        }
        dp.put(i, minimumPartitions);
        return dp.get(i);
    }

    public static Integer palindromePartitioning(String string) {
        /*
            Time complexity is O(n^2 * m) and space complexity is O(n + n*m), where m is the longest substring length.
         */
        int n = string.length();

        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            dp.put(i, null);
        }

        return solve(string, 0, n, dp) - 1;
    }
}
