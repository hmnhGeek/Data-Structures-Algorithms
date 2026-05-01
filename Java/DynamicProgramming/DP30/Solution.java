package DynamicProgramming.DP30;


public class Solution {
    public static void main(String[] args) {
        recursive();
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
}
