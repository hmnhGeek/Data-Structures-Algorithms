package Strings.RecursivelyPrintSentences;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    private static void createSentences(List<List<String>> words, Integer i, List<String> sentence, List<String> sentences) {
        if (i.equals(words.size())) {
            sentences.add(String.join(" ", sentence));
            return;
        }
        for (int j = 0; j < words.get(i).size(); j += 1) {
            sentence.add(words.get(i).get(j));
            createSentences(words, i + 1, sentence, sentences);
            sentence.removeLast();
        }
    }

    public static List<String> createSentences(List<List<String>> words) {
        List<String> sentence = new ArrayList<>();
        List<String> sentences = new ArrayList<>();
        createSentences(words, 0, sentence, sentences);
        return sentences;
    }

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
    }
}
