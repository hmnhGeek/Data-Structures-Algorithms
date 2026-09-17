package Strings.Problem23;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getCountInGrid(List<List<Character>> mtx, String word) {
        int n = mtx.size(), m = mtx.getFirst().size();
        int size = word.length();
        int count = 0;
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                count += solve(i, j, word, mtx, 0, n, m, size);
            }
        }
        return count;
    }

    private static Integer solve(int i, int j, String word, List<List<Character>> mtx, int idx, int n, int m, int size) {
        int found = 0;
        if (i >= 0 && i < n && j >= 0 && j < m && mtx.get(i).get(j) == word.charAt(idx)) {
            Character temp = word.charAt(idx);
            mtx.get(i).set(j, '0');
            idx += 1;
            if (idx == size) {
                found = 1;
            } else {
                found += solve(i - 1, j, word, mtx, idx, n, m, size);
                found += solve(i, j + 1, word, mtx, idx, n, m, size);
                found += solve(i + 1, j, word, mtx, idx, n, m, size);
                found += solve(i, j - 1, word, mtx, idx, n, m, size);
            }
            mtx.get(i).set(j, temp);
        }
        return found;
    }

    public static void main(String[] args) {
        List<List<Character>> matrix = Arrays.asList(
                Arrays.asList('S', 'N', 'B', 'S', 'N'),
                Arrays.asList('B', 'A', 'K', 'E', 'A'),
                Arrays.asList('B', 'K', 'B', 'B', 'K'),
                Arrays.asList('S', 'E', 'B', 'S', 'E')
        );
        String word = "SNAKE";
        System.out.println(getCountInGrid(matrix, word));

        List<List<Character>> matrix2 = Arrays.asList(
                Arrays.asList('a', 'x', 'm', 'y'),
                Arrays.asList('b', 'g', 'd', 'j'),
                Arrays.asList('x', 'e', 'e', 't'),
                Arrays.asList('r', 'a', 'k', 's')
        );
        String word2 = "geeks";
        System.out.println(getCountInGrid(matrix2, word2));
    }
}
