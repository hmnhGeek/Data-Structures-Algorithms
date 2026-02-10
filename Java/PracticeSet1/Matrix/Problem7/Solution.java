// Problem link - https://www.geeksforgeeks.org/dsa/find-a-specific-pair-in-matrix/
// Solution - https://www.youtube.com/watch?v=aUhR_T5J9is


package PracticeSet1.Matrix.Problem7;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<List<Integer>> matrix = List.of(
                List.of(1, 2, -1, -4, -20),
                List.of(-8, -3, 4, 2, 1),
                List.of(3, 8, 6, 1, 3),
                List.of(-4, -1, 1, 7, -6),
                List.of(0, -4, 10, -5, 1)
        );

        System.out.println(getSpecificPairDifference(matrix));

        List<List<Integer>> matrix2 = List.of(
                List.of(7, -8, 9, 11, 2, -6),
                List.of(1, 2, 0, 9, -11, 6),
                List.of(9, 10, 23, -6, 7, 2),
                List.of(9, -13, 20, 17, 6, 3),
                List.of(0, 2, 16, 0, -2, 8),
                List.of(-1, 2, 7, 12, 13, -3)
        );

        System.out.println(getSpecificPairDifference(matrix2));
    }

    public static Integer getSpecificPairDifference(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm) and space complexity is O(nm).
         */
        int n = mtx.size();
        List<List<Integer>> maxMatrix = getMaxMatrix(mtx, n);
        Integer result = Integer.MIN_VALUE;
        for (int i = 0; i < n - 1; i += 1) {
            for (int j = 0; j < n - 1; j += 1) {
                result = Math.max(result, maxMatrix.get(i + 1).get(j + 1) - mtx.get(i).get(j));
            }
        }
        return result;
    }

    private static List<List<Integer>> getMaxMatrix(List<List<Integer>> mtx, int n) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j += 1) {
                row.add(null);
            }
            result.add(row);
        }
        result.get(n - 1).set(n - 1, mtx.get(n - 1).get(n - 1));
        for (int i = n - 2; i >= 0; i -= 1) {
            result.get(i).set(n - 1, Math.max(result.get(i + 1).get(n - 1), mtx.get(i).get(n - 1)));
        }
        for (int j = n - 2; j >= 0; j -= 1) {
            result.get(n - 1).set(j, Math.max(result.get(n - 1).get(j + 1), mtx.get(n - 1).get(j)));
        }
        for (int i = n - 2; i >= 0; i -= 1) {
            for (int j = n - 2; j >= 0; j -= 1) {
                result.get(i).set(
                        j,
                        Math.max(
                                mtx.get(i).get(j),
                                Math.max(
                                        result.get(i).get(j + 1),
                                        result.get(i + 1).get(j)
                                )
                        )
                );
            }
        }
        return result;
    }
}
