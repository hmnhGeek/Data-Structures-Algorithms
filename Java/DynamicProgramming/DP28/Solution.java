package DynamicProgramming.DP28;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        System.out.println(RecursiveSolution.getLcsLength("adebc", "dcadb"));
        System.out.println(RecursiveSolution.getLcsLength("ab", "defg"));
        System.out.println(RecursiveSolution.getLcsLength("abcde", "ace"));
        System.out.println(RecursiveSolution.getLcsLength("abc", "abc"));
        System.out.println(RecursiveSolution.getLcsLength("abc", "acd"));
        System.out.println(RecursiveSolution.getLcsLength("AGGTAB", "GXTXAYB"));
        System.out.println(RecursiveSolution.getLcsLength("ABC", "CBA"));

        System.out.println();
        System.out.println(MemoizedSolution.getLcsLength("adebc", "dcadb"));
        System.out.println(MemoizedSolution.getLcsLength("ab", "defg"));
        System.out.println(MemoizedSolution.getLcsLength("abcde", "ace"));
        System.out.println(MemoizedSolution.getLcsLength("abc", "abc"));
        System.out.println(MemoizedSolution.getLcsLength("abc", "acd"));
        System.out.println(MemoizedSolution.getLcsLength("AGGTAB", "GXTXAYB"));
        System.out.println(MemoizedSolution.getLcsLength("ABC", "CBA"));

        System.out.println();
        System.out.println(TabulationSolution.getLcsLength("adebc", "dcadb"));
        System.out.println(TabulationSolution.getLcsLength("ab", "defg"));
        System.out.println(TabulationSolution.getLcsLength("abcde", "ace"));
        System.out.println(TabulationSolution.getLcsLength("abc", "abc"));
        System.out.println(TabulationSolution.getLcsLength("abc", "acd"));
        System.out.println(TabulationSolution.getLcsLength("AGGTAB", "GXTXAYB"));
        System.out.println(TabulationSolution.getLcsLength("ABC", "CBA"));

        System.out.println();
        System.out.println(SpaceOptimizedSolution.getLcsLength("adebc", "dcadb"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("ab", "defg"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("abcde", "ace"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("abc", "abc"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("abc", "acd"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("AGGTAB", "GXTXAYB"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("ABC", "CBA"));

        System.out.println();
        System.out.println(getLCS("adebc", "dcadb"));
        System.out.println(getLCS("ab", "defg"));
        System.out.println(getLCS("abcde", "ace"));
        System.out.println(getLCS("abc", "abc"));
        System.out.println(getLCS("abc", "acd"));
        System.out.println(getLCS("AGGTAB", "GXTXAYB"));
        System.out.println(getLCS("ABC", "CBA"));
    }

    public static String getLCS(String s1, String s2) {
        /*
            Time complexity is O(mn) and space complexity is O(mn).
         */
            int n1 = s1.length(), n2 = s2.length();
            Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
            for (int i = 0; i <= n1; i += 1) {
                Map<Integer, Integer> prev = new HashMap<>();
                for (int j = 0; j <= n2; j += 1) {
                    prev.put(j, 0);
                }
                dp.put(i, prev);
            }

            for (int i = 1; i <= n1; i += 1) {
                for (int j = 1; j <= n2; j += 1) {
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

            int i = n1, j = n2;
            StringBuilder result = new StringBuilder();
            while (i > 0 && j > 0) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    result.append(s1.charAt(i - 1));
                    i -= 1;
                    j -= 1;
                } else if (dp.get(i - 1).get(j) > dp.get(i).get(j - 1)) {
                    i -= 1;
                } else {
                    j -= 1;
                }
            }
            result.reverse();
            return result.toString();
    }
}
