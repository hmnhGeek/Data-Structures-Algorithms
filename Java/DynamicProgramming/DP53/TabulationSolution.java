package DynamicProgramming.DP53;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    public static Integer palindromePartitioning(String string) {
        /*
            Time complexity is O(n^2 * m) and space complexity is O(n*m), where m is the longest substring length.
         */
        int n = string.length();

        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            dp.put(i, Integer.MAX_VALUE);
        }
        dp.put(n, 0);

        for (int i = n - 1; i >= 0; i -= 1) {
            Integer minimumPartitions = Integer.MAX_VALUE;
            StringBuilder temp = new StringBuilder();
            for (int j = i; j < n; j += 1) {
                temp.append(string.charAt(j));
                if (PalindromeChecker.isPalindrome(String.valueOf(temp))) {
                    Integer partitions = 1 + dp.get(j + 1);
                    minimumPartitions = Math.min(minimumPartitions, partitions);
                }
            }
            dp.put(i, minimumPartitions);
        }

        return dp.get(0) - 1;
    }
}
