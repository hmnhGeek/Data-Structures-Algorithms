package DynamicProgramming.DP27;

public class Solution {
    public static void main(String[] args) {
        // Tabulation Solution
        System.out.println(
                TabulationSolution.getLongestCommonSubstringLength("abcd", "abzd")
        );

        System.out.println(
                TabulationSolution.getLongestCommonSubstringLength("abcjklp", "acjkp")
        );

        System.out.println(
                TabulationSolution.getLongestCommonSubstringLength("wasdijkl", "wsdjkl")
        );

        System.out.println(
                TabulationSolution.getLongestCommonSubstringLength("tyfg", "cvbnuty")
        );

        System.out.println(
                TabulationSolution.getLongestCommonSubstringLength("GeeksforGeeks", "GeeksQuiz")
        );

        System.out.println(
                TabulationSolution.getLongestCommonSubstringLength("abcdxyz", "xyzabcd")
        );

        System.out.println(
                TabulationSolution.getLongestCommonSubstringLength("abc", "")
        );
    }
}
