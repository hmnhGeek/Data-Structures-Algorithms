package Strings.RecursivelyPrintSentences;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    private static void createSentences(List<List<String>> words, Integer i, List<String> sentence, List<String> sentences) {
        // base case
        if (i.equals(words.size())) {
            sentences.add(String.join(" ", sentence));
            return;
        }
        for (int j = 0; j < words.get(i).size(); j += 1) {
            // add the current word to sentence list.
            sentence.add(words.get(i).get(j));
            // recursively check words from next row.
            createSentences(words, i + 1, sentence, sentences);
            // while backtracking, remove the added word.
            sentence.removeLast();
        }
    }

    public static List<String> createSentences(List<List<String>> words) {
        List<String> sentence = new ArrayList<>();
        List<String> sentences = new ArrayList<>();
        createSentences(words, 0, sentence, sentences);
        return sentences;
    }

    /**
     * A utility method to print sentences correctly.
     * @param words
     */
    public static void formSentences(List<List<String>> words) {
        List<String> sentences = createSentences(words);
        for (String sentence : sentences) {
            System.out.println(sentence);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        formSentences(Arrays.asList(
                Arrays.asList("you", "we"),
                Arrays.asList("have", "are"),
                Arrays.asList("sleep", "eat", "drink")
        ));
        formSentences(
                Arrays.asList(
                        Arrays.asList("you", "we"),
                        Arrays.asList("have", "are")
                )
        );
        formSentences(
                Arrays.asList(
                        Arrays.asList("I", "You"),
                        Arrays.asList("Do", "do not like"),
                        Arrays.asList("walking", "eating")
                )
        );
        formSentences(
                Arrays.asList(
                        Arrays.asList("work", "live"),
                        Arrays.asList("easy", "happily")
                )
        );
    }
}
