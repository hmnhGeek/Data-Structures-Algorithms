package DynamicProgramming.DP25;

public class Solution {
    private static void recursive() {
        System.out.println(RecursiveSolution.getLcs("adebc", "dcadb"));
        System.out.println(RecursiveSolution.getLcs("ab", "defg"));
        System.out.println(RecursiveSolution.getLcs("abcde", "ace"));
        System.out.println(RecursiveSolution.getLcs("abc", "abc"));
        System.out.println(RecursiveSolution.getLcs("abc", "acd"));
        System.out.println(RecursiveSolution.getLcs("AGGTAB", "GXTXAYB"));
        System.out.println(RecursiveSolution.getLcs("ABC", "CBA"));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getLcs("adebc", "dcadb"));
        System.out.println(MemoizedSolution.getLcs("ab", "defg"));
        System.out.println(MemoizedSolution.getLcs("abcde", "ace"));
        System.out.println(MemoizedSolution.getLcs("abc", "abc"));
        System.out.println(MemoizedSolution.getLcs("abc", "acd"));
        System.out.println(MemoizedSolution.getLcs("AGGTAB", "GXTXAYB"));
        System.out.println(MemoizedSolution.getLcs("ABC", "CBA"));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
    }
}
