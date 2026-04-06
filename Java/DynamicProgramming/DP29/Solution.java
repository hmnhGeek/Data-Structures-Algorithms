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

    public static void main(String[] args) {
        recursive();
        memoized();
    }
}
