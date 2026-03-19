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


        System.out.println();


        // Space Optimized Solution
        System.out.println(
                SpaceOptimizedSolution.getLongestCommonSubstringLength("abcd", "abzd")
        );

        System.out.println(
                SpaceOptimizedSolution.getLongestCommonSubstringLength("abcjklp", "acjkp")
        );

        System.out.println(
                SpaceOptimizedSolution.getLongestCommonSubstringLength("wasdijkl", "wsdjkl")
        );

        System.out.println(
                SpaceOptimizedSolution.getLongestCommonSubstringLength("tyfg", "cvbnuty")
        );

        System.out.println(
                SpaceOptimizedSolution.getLongestCommonSubstringLength("GeeksforGeeks", "GeeksQuiz")
        );

        System.out.println(
                SpaceOptimizedSolution.getLongestCommonSubstringLength("abcdxyz", "xyzabcd")
        );

        System.out.println(
                SpaceOptimizedSolution.getLongestCommonSubstringLength("abc", "")
        );
    }
}
