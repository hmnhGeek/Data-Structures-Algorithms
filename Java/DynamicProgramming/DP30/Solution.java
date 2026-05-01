// Problem link - https://www.naukri.com/code360/problems/can-you-make_4244510?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=yMnH0jrir0Q&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=31


package DynamicProgramming.DP30;


public class Solution {
    public static void main(String[] args) {
        recursive();
        System.out.println();
        memoized();
        System.out.println();
        tabulation();
        System.out.println();
        spaceOptimized();
        System.out.println();

        System.out.println(Solution.getMinOps("abcd", "anc"));
        System.out.println(Solution.getMinOps("aaa", "aa"));
        System.out.println(Solution.getMinOps("edl", "xcqja"));
        System.out.println(Solution.getMinOps("heap", "pea"));
        System.out.println(Solution.getMinOps("geeksforgeeks", "geeks"));
    }

    private static void recursive() {
        System.out.println(RecursiveSolution.getLcsLength("adebc", "dcadb"));
        System.out.println(RecursiveSolution.getLcsLength("ab", "defg"));
        System.out.println(RecursiveSolution.getLcsLength("abcde", "ace"));
        System.out.println(RecursiveSolution.getLcsLength("abc", "abc"));
        System.out.println(RecursiveSolution.getLcsLength("abc", "acd"));
        System.out.println(RecursiveSolution.getLcsLength("AGGTAB", "GXTXAYB"));
        System.out.println(RecursiveSolution.getLcsLength("ABC", "CBA"));
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getLcsLength("adebc", "dcadb"));
        System.out.println(MemoizedSolution.getLcsLength("ab", "defg"));
        System.out.println(MemoizedSolution.getLcsLength("abcde", "ace"));
        System.out.println(MemoizedSolution.getLcsLength("abc", "abc"));
        System.out.println(MemoizedSolution.getLcsLength("abc", "acd"));
        System.out.println(MemoizedSolution.getLcsLength("AGGTAB", "GXTXAYB"));
        System.out.println(MemoizedSolution.getLcsLength("ABC", "CBA"));
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getLcsLength("adebc", "dcadb"));
        System.out.println(TabulationSolution.getLcsLength("ab", "defg"));
        System.out.println(TabulationSolution.getLcsLength("abcde", "ace"));
        System.out.println(TabulationSolution.getLcsLength("abc", "abc"));
        System.out.println(TabulationSolution.getLcsLength("abc", "acd"));
        System.out.println(TabulationSolution.getLcsLength("AGGTAB", "GXTXAYB"));
        System.out.println(TabulationSolution.getLcsLength("ABC", "CBA"));
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getLcsLength("adebc", "dcadb"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("ab", "defg"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("abcde", "ace"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("abc", "abc"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("abc", "acd"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("AGGTAB", "GXTXAYB"));
        System.out.println(SpaceOptimizedSolution.getLcsLength("ABC", "CBA"));
    }

    public static Integer getMinOps(String s1, String s2) {
        int lcsLength = SpaceOptimizedSolution.getLcsLength(s1, s2);
        return s1.length() + s2.length() - 2*lcsLength;
    }
}
