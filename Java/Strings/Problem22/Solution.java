package Strings.Problem22;

public class Solution {
    private static void recursive() {
        System.out.println(RecursiveSolution.countPalindromicSubsequences("abcd"));
        System.out.println(RecursiveSolution.countPalindromicSubsequences("aab"));
        System.out.println(RecursiveSolution.countPalindromicSubsequences("b"));
        System.out.println(RecursiveSolution.countPalindromicSubsequences("103301"));
        System.out.println(RecursiveSolution.countPalindromicSubsequences("0000000"));
        System.out.println(RecursiveSolution.countPalindromicSubsequences("9999900000"));
        System.out.println(RecursiveSolution.countPalindromicSubsequences("bccb"));
        System.out.println(RecursiveSolution.countPalindromicSubsequences("pqqr"));
        System.out.println(RecursiveSolution.countPalindromicSubsequences("aaaa"));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.countPalindromicSubsequences("abcd"));
        System.out.println(MemoizedSolution.countPalindromicSubsequences("aab"));
        System.out.println(MemoizedSolution.countPalindromicSubsequences("b"));
        System.out.println(MemoizedSolution.countPalindromicSubsequences("103301"));
        System.out.println(MemoizedSolution.countPalindromicSubsequences("0000000"));
        System.out.println(MemoizedSolution.countPalindromicSubsequences("9999900000"));
        System.out.println(MemoizedSolution.countPalindromicSubsequences("bccb"));
        System.out.println(MemoizedSolution.countPalindromicSubsequences("pqqr"));
        System.out.println(MemoizedSolution.countPalindromicSubsequences("aaaa"));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.countPalindromicSubsequences("abcd"));
        System.out.println(TabulationSolution.countPalindromicSubsequences("aab"));
        System.out.println(TabulationSolution.countPalindromicSubsequences("b"));
        System.out.println(TabulationSolution.countPalindromicSubsequences("103301"));
        System.out.println(TabulationSolution.countPalindromicSubsequences("0000000"));
        System.out.println(TabulationSolution.countPalindromicSubsequences("9999900000"));
        System.out.println(TabulationSolution.countPalindromicSubsequences("bccb"));
        System.out.println(TabulationSolution.countPalindromicSubsequences("pqqr"));
        System.out.println(TabulationSolution.countPalindromicSubsequences("aaaa"));
        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.countPalindromicSubsequences("abcd"));
        System.out.println(SpaceOptimizedSolution.countPalindromicSubsequences("aab"));
        System.out.println(SpaceOptimizedSolution.countPalindromicSubsequences("b"));
        System.out.println(SpaceOptimizedSolution.countPalindromicSubsequences("103301"));
        System.out.println(SpaceOptimizedSolution.countPalindromicSubsequences("0000000"));
        System.out.println(SpaceOptimizedSolution.countPalindromicSubsequences("9999900000"));
        System.out.println(SpaceOptimizedSolution.countPalindromicSubsequences("bccb"));
        System.out.println(SpaceOptimizedSolution.countPalindromicSubsequences("pqqr"));
        System.out.println(SpaceOptimizedSolution.countPalindromicSubsequences("aaaa"));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }
}
