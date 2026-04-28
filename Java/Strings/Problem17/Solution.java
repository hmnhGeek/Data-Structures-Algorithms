package Strings.Problem17;

import java.util.Arrays;

public class Solution {
    private static void recursive() {
        System.out.println(
                RecursiveSolution.wordBreak(
                        "ilike",
                        Arrays.asList("i", "like", "sam", "sung", "samsung", "mobile")
                )
        );

        System.out.println(
                RecursiveSolution.wordBreak(
                        "ilikesamsung",
                        Arrays.asList("i", "like", "sam", "sung", "samsung", "mobile")
                )
        );

        System.out.println(
                RecursiveSolution.wordBreak(
                        "catsandog",
                        Arrays.asList("cats", "dog", "sand", "and", "cat")
                )
        );

        System.out.println(
                RecursiveSolution.wordBreak(
                        "storybook",
                        Arrays.asList("story", "book")
                )
        );

        System.out.println(
                RecursiveSolution.wordBreak(
                        "monkeyandonkey",
                        Arrays.asList("monkey", "donkey", "and")
                )
        );

        System.out.println(
                RecursiveSolution.wordBreak(
                        "applepenapple",
                        Arrays.asList("apple", "pen")
                )
        );
    }

    public static void main(String[] args) {
        recursive();
        System.out.println();
    }
}
