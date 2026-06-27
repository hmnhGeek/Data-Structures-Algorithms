package DynamicProgramming.DP34;

public class Solution {
    private static void recursive() {
        System.out.println(RecursiveSolution.isMatching("?ay", "ray"));
        System.out.println(RecursiveSolution.isMatching("ab*cd", "abdefcd"));
        System.out.println(RecursiveSolution.isMatching("ab?d", "abcc"));
        System.out.println(RecursiveSolution.isMatching("ba*a?", "baaabab"));
        System.out.println(RecursiveSolution.isMatching("a", "aa"));
        System.out.println(RecursiveSolution.isMatching("*", "aa"));
        System.out.println(RecursiveSolution.isMatching("?a", "cb"));
        System.out.println(RecursiveSolution.isMatching("**", ""));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.isMatching("?ay", "ray"));
        System.out.println(MemoizedSolution.isMatching("ab*cd", "abdefcd"));
        System.out.println(MemoizedSolution.isMatching("ab?d", "abcc"));
        System.out.println(MemoizedSolution.isMatching("ba*a?", "baaabab"));
        System.out.println(MemoizedSolution.isMatching("a", "aa"));
        System.out.println(MemoizedSolution.isMatching("*", "aa"));
        System.out.println(MemoizedSolution.isMatching("?a", "cb"));
        System.out.println(MemoizedSolution.isMatching("**", ""));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.isMatching("?ay", "ray"));
        System.out.println(TabulationSolution.isMatching("ab*cd", "abdefcd"));
        System.out.println(TabulationSolution.isMatching("ab?d", "abcc"));
        System.out.println(TabulationSolution.isMatching("ba*a?", "baaabab"));
        System.out.println(TabulationSolution.isMatching("a", "aa"));
        System.out.println(TabulationSolution.isMatching("*", "aa"));
        System.out.println(TabulationSolution.isMatching("?a", "cb"));
        System.out.println(TabulationSolution.isMatching("**", ""));
        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.isMatching("?ay", "ray"));
        System.out.println(SpaceOptimizedSolution.isMatching("ab*cd", "abdefcd"));
        System.out.println(SpaceOptimizedSolution.isMatching("ab?d", "abcc"));
        System.out.println(SpaceOptimizedSolution.isMatching("ba*a?", "baaabab"));
        System.out.println(SpaceOptimizedSolution.isMatching("a", "aa"));
        System.out.println(SpaceOptimizedSolution.isMatching("*", "aa"));
        System.out.println(SpaceOptimizedSolution.isMatching("?a", "cb"));
        System.out.println(SpaceOptimizedSolution.isMatching("**", ""));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }
}
