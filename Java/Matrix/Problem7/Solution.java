// Problem link - https://www.geeksforgeeks.org/dsa/find-a-specific-pair-in-matrix/
// Solution - https://www.youtube.com/watch?v=aUhR_T5J9is

package Matrix.Problem7;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static Integer findSpecificPair(List<List<Integer>> matrix) {
        /*
            Time complexity is O(nm) and space complexity is O(nm).
         */

        int n = matrix.size(), m = matrix.getFirst().size();
        List<List<Integer>> maxMatrix = getMaxMatrix(matrix, n, m);
        for (int i = n - 2; i >= 0; i -= 1) {
            maxMatrix.get(i).set(
                    m - 1,
                    Math.max(matrix.get(i).get(m - 1), maxMatrix.get(i + 1).get(m - 1))
            );
        }
        for (int j = m - 2; j >= 0; j -= 1) {
            maxMatrix.get(n - 1).set(
                    j,
                    Math.max(matrix.get(n - 1).get(j), maxMatrix.get(n - 1).get(j + 1))
            );
        }
        for (int i = n - 2; i >= 0; i -= 1) {
            for (int j = m - 2; j >= 0; j -= 1) {
                maxMatrix.get(i).set(
                        j,
                        Math.max(
                            Math.max(
                                matrix.get(i).get(j),
                                maxMatrix.get(i).get(j + 1)
                            ),
                            maxMatrix.get(i + 1).get(j)
                        )
                );
            }
        }
        Integer result = Integer.MIN_VALUE;
        for (int i = 0; i < n - 1; i += 1) {
            for (int j = 0; j < m - 1; j += 1) {
                result = Math.max(result, maxMatrix.get(i + 1).get(j + 1) - matrix.get(i).get(j));
            }
        }
        return result;
    }

    private static List<List<Integer>> getMaxMatrix(List<List<Integer>> matrix, int n, int m) {
        List<List<Integer>> maxMatrix = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(null);
            }
            maxMatrix.add(row);
        }
        maxMatrix.get(n - 1).set(m - 1, matrix.getLast().getLast());
        return maxMatrix;
    }

    public static void main(String[] args) {
        List<List<Integer>> matrix = List.of(
                List.of(1, 2, -1, -4, -20),
                List.of(-8, -3, 4, 2, 1),
                List.of(3, 8, 6, 1, 3),
                List.of(-4, -1, 1, 7, -6),
                List.of(0, -4, 10, -5, 1)
        );

        System.out.println(Solution.findSpecificPair(matrix));

        List<List<Integer>> matrix2 = List.of(
                List.of(7, -8, 9, 11, 2, -6),
                List.of(1, 2, 0, 9, -11, 6),
                List.of(9, 10, 23, -6, 7, 2),
                List.of(9, -13, 20, 17, 6, 3),
                List.of(0, 2, 16, 0, -2, 8),
                List.of(-1, 2, 7, 12, 13, -3)
        );

        System.out.println(Solution.findSpecificPair(matrix2));
    }
}
