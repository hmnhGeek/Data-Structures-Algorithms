package Graphs.G30;

import java.util.*;

public class WordLadder {
    public static List<List<String>> getWordLadder(List<String> words, String startWord, String endWord) {
        if (!words.contains(endWord)) return new ArrayList<>();
        Queue<List<String>> queue = new Queue<>();
        List<String> usedOnLevel = new ArrayList<>();
        List<List<String>> result = new ArrayList<>();

        queue.push(Arrays.asList(startWord));
        usedOnLevel.add(startWord);

        Set<String> visited = new HashSet<>(words);
        int level = 0;

        while (!queue.isEmpty()) {
            List<String> vector = queue.pop();

            if (vector.size() > level) {
                for (String usedWord : usedOnLevel) {
                    visited.remove(usedWord);
                }
                level += 1;
                usedOnLevel.clear();
            }

            String currentWord = vector.getLast();

            if (Objects.equals(currentWord, endWord)) {
                if (result.isEmpty()) {
                    result.add(vector);
                } else if (vector.size() == result.getFirst().size()) {
                    result.add(vector);
                }
            }

            String originalWord = vector.getLast();

            for (int i = 0; i < currentWord.length(); i += 1) {
                for (Character character : "abcdefghijklmnopqrstuvwxyz".toCharArray()) {
                    char[] charArray = currentWord.toCharArray();
                    charArray[i] = character;
                    currentWord = String.valueOf(charArray);

                    if (visited.contains(currentWord)) {
                        List<String> newVector = new ArrayList<>(vector.stream().toList());
                        newVector.add(currentWord);
                        queue.push(newVector);
                        usedOnLevel.add(currentWord);
                    }
                }
                currentWord = originalWord;
            }

        }
        return result;
    }
}
