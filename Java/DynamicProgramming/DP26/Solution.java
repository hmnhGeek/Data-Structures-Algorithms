package DynamicProgramming.DP26;

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
    }
}
