package Graphs.G29;

import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;


class Ladder {
    public String word;
    public Integer length;

    public Ladder(Integer length, String word) {
        this.length = length;
        this.word = word;
    }
}


public class WordLadder {
    public static Integer getMinimumLength(List<String> words, String startWord, String endWord) {
        if (!words.contains(endWord)) return 0;
        Set<String> visited = new HashSet<>(words);
        Queue<Ladder> queue = new Queue<>();
        queue.push(new Ladder(1, startWord));
        visited.remove(startWord);
        while (!queue.isEmpty()) {
            Ladder poppedLadder = queue.pop();
            String currentWord = poppedLadder.word;
            if (Objects.equals(currentWord, endWord)) {
                return poppedLadder.length;
            }
            String originalWord = poppedLadder.word;
            for (int i = 0; i < currentWord.length(); i += 1) {
                for (Character c : "abcdefghijklmnopqrstuvwxyz".toCharArray()) {
                    char[] charArray = currentWord.toCharArray();
                    charArray[i] = c;
                    currentWord = String.valueOf(charArray);
                    if (visited.contains(currentWord)) {
                        visited.remove(currentWord);
                        queue.push(new Ladder(poppedLadder.length + 1, currentWord));
                    }
                }
                currentWord = originalWord;

            }
        }
        return 0;
    }
}
