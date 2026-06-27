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

    public static void main(String[] args) {
        recursive();
    }
}
