// Problem link - https://www.geeksforgeeks.org/dsa/common-elements-in-all-rows-of-a-given-matrix/


package Matrix.Problem10;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {
    public static Set<Integer> commonElements(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        Set<Integer> set = new HashSet<>(mtx.getFirst());
        Set<Integer> nonAnswers = new HashSet<>();
        for (int i = 1; i < n; i += 1) {
            for (Integer val : set) {
                if (!mtx.get(i).contains(val)) {
                    nonAnswers.add(val);
                }
            }
        }
        set.removeAll(nonAnswers);
        return set;
    }

    public static void main(String[] args) {
        List<List<Integer>> matrix = Arrays.asList(
                Arrays.asList(1, 2, 1, 4, 8),
                Arrays.asList(3, 7, 8, 5, 1),
                Arrays.asList(8, 7, 7, 3, 1),
                Arrays.asList(8, 1, 2, 7, 9)
        );
        System.out.println(commonElements(matrix));
    }
}
