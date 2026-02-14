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

    public static void main(String[] args) {
        recursive();
    }
}
