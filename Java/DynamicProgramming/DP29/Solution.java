// Problem link - https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
// Solution - https://www.youtube.com/watch?v=xPBLEj41rFU&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=30


package DynamicProgramming.DP29;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getMinCharToMakePalindrome("abca"));
        System.out.println(RecursiveSolution.getMinCharToMakePalindrome("abcdefg"));
        System.out.println(RecursiveSolution.getMinCharToMakePalindrome("aaaaa"));
        System.out.println(RecursiveSolution.getMinCharToMakePalindrome("zzazz"));
        System.out.println(RecursiveSolution.getMinCharToMakePalindrome("mbadm"));
        System.out.println(RecursiveSolution.getMinCharToMakePalindrome("leetcode"));
        System.out.println();
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.getMinCharToMakePalindrome("abca"));
        System.out.println(MemoizedSolution.getMinCharToMakePalindrome("abcdefg"));
        System.out.println(MemoizedSolution.getMinCharToMakePalindrome("aaaaa"));
        System.out.println(MemoizedSolution.getMinCharToMakePalindrome("zzazz"));
        System.out.println(MemoizedSolution.getMinCharToMakePalindrome("mbadm"));
        System.out.println(MemoizedSolution.getMinCharToMakePalindrome("leetcode"));
        System.out.println();
    }

    public static void tabulation() {
        System.out.println(TabulationSolution.getMinCharToMakePalindrome("abca"));
        System.out.println(TabulationSolution.getMinCharToMakePalindrome("abcdefg"));
        System.out.println(TabulationSolution.getMinCharToMakePalindrome("aaaaa"));
        System.out.println(TabulationSolution.getMinCharToMakePalindrome("zzazz"));
        System.out.println(TabulationSolution.getMinCharToMakePalindrome("mbadm"));
        System.out.println(TabulationSolution.getMinCharToMakePalindrome("leetcode"));
        System.out.println();
    }

    public static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getMinCharToMakePalindrome("abca"));
        System.out.println(SpaceOptimizedSolution.getMinCharToMakePalindrome("abcdefg"));
        System.out.println(SpaceOptimizedSolution.getMinCharToMakePalindrome("aaaaa"));
        System.out.println(SpaceOptimizedSolution.getMinCharToMakePalindrome("zzazz"));
        System.out.println(SpaceOptimizedSolution.getMinCharToMakePalindrome("mbadm"));
        System.out.println(SpaceOptimizedSolution.getMinCharToMakePalindrome("leetcode"));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }
}
