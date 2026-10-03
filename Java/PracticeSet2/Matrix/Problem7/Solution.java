package PracticeSet2.Matrix.Problem7;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static Integer getSpecificPairDifference(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        List<List<Integer>> maxMtx = getMaxMtx(n, m);
        maxMtx.get(n - 1).set(m - 1, mtx.getLast().getLast());

        // set last column
        for (int i = n - 2; i >= 0; i -= 1) {
            maxMtx.get(i).set(m - 1, Math.max(mtx.get(i).get(m - 1), maxMtx.get(i + 1).get(m - 1)));
        }

        // set last row
        for (int j = m - 2; j >= 0; j -= 1) {
            maxMtx.get(n - 1).set(j, Math.max(mtx.get(n - 1).get(j), maxMtx.get(n - 1).get(j + 1)));
        }

        for (int i = n - 2; i >= 0; i -= 1) {
            for (int j = m - 2; j >= 0; j -= 1) {
                maxMtx.get(i).set(
                        j,
                        Math.max(
                                mtx.get(i).get(j),
                                Math.max(maxMtx.get(i + 1).get(j), maxMtx.get(i).get(j + 1))
                        )
                );
            }
        }

        int result = Integer.MIN_VALUE;
        for (int i = 0; i < n - 1; i += 1) {
            for (int j = 0; j < m - 1; j += 1) {
                result = Math.max(result, maxMtx.get(i + 1).get(j + 1) - mtx.get(i).get(j));
            }
        }
        return result;
    }

    private static List<List<Integer>> getMaxMtx(int n, int m) {
        List<List<Integer>> maxMtx = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(null);
            }
            maxMtx.add(row);
        }
        return maxMtx;
    }

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
}
