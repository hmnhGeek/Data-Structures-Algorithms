package Strings.Problem24;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<List<Integer>> getAllOccurrences(List<List<Character>> mtx, String word) {
        int n = mtx.size(), m = mtx.getFirst().size();
        List<Integer> dr = Arrays.asList(-1, -1, 0, 1, 1, 1, 0, -1);
        List<Integer> dc = Arrays.asList(0, 1, 1, 1, 0, -1, -1, -1);
        List<List<Integer>> result = new ArrayList<>();
        for (int r = 0; r < n; r += 1) {
            for (int c = 0; c < m; c += 1) {
                if (word.charAt(0) != mtx.get(r).get(c)) {
                    continue;
                }
                for (int d = 0; d < 8; d += 1) {
                    int drVal = dr.get(d);
                    int dcVal = dc.get(d);
                    boolean found = true;
                    for (int k = 0; k < word.length(); k += 1) {
                        int nr = r + (k * drVal);
                        int nc = c + (k * dcVal);
                        if (!(0 <= nr && nr < n && 0 <= nc && nc < m)) {
                            found = false;
                            break;
                        }
                        if (mtx.get(nr).get(nc) != word.charAt(k)) {
                            found = false;
                            break;
                        }
                    }
                    if (found) {
                        result.add(List.of(r, c));
                        break;
                    }
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {

        List<List<Character>> mat1 = Arrays.asList(
                Arrays.asList('a', 'b', 'a', 'b'),
                Arrays.asList('a', 'b', 'e', 'b'),
                Arrays.asList('e', 'b', 'e', 'b')
        );
        String word1 = "abe";

        System.out.println(getAllOccurrences(mat1, word1));


        List<List<Character>> mat2 = Arrays.asList(
                Arrays.asList('G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S'),
                Arrays.asList('G', 'E', 'E', 'K', 'S', 'Q', 'U', 'I', 'Z', 'G', 'E', 'E', 'K'),
                Arrays.asList('I', 'D', 'E', 'Q', 'A', 'P', 'R', 'A', 'C', 'T', 'I', 'C', 'E')
        );
        String word2 = "GEEKS";

        System.out.println(getAllOccurrences(mat2, word2));
    }
}
