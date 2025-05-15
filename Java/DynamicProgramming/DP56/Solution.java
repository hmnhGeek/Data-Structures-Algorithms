package DynamicProgramming.DP56;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static Integer countSquareSubMatrices(List<List<Integer>> matrix) {
        int n = matrix.size(), m = matrix.getFirst().size();
        List<List<Integer>> dp = getDpMatrix(matrix);
        for (int i = 1; i < n; i += 1) {
            for (int j = 1; j < m; j += 1) {
                if (matrix.get(i).get(j).equals(0)) {
                    dp.get(i).set(j, 0);
                } else {
                    dp.get(i).set(j, 1 + Math.min(
                            dp.get(i - 1).get(j),
                            Math.min(dp.get(i - 1).get(j - 1), dp.get(i).get(j - 1))
                    ));
                }
            }
        }
        Integer sum = 0;
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                sum += dp.get(i).get(j);
            }
        }
        return sum;
    }

    private static List<List<Integer>> getDpMatrix(List<List<Integer>> matrix) {
        int n = matrix.size(), m = matrix.getFirst().size();
        List<List<Integer>> dp = new ArrayList<>();
        List<Integer> row = new ArrayList<>();
        for (int j = 0; j < m; j += 1) {
            row.add(matrix.getFirst().get(j));
        }
        dp.add(row);
        for (int i = 1; i < n; i += 1) {
            List<Integer> r = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                if (j == 0) r.add(matrix.get(i).getFirst());
                else {
                    r.add(0);
                }
            }
            dp.add(r);
        }
        return dp;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.countSquareSubMatrices(
                        List.of(
                                List.of(1, 1),
                                List.of(1, 1)
                        )
                )
        );

        System.out.println(
                Solution.countSquareSubMatrices(
                        List.of(
                                List.of(1, 0),
                                List.of(0, 1)
                        )
                )
        );

        System.out.println(
                Solution.countSquareSubMatrices(
                        List.of(
                                List.of(0, 1, 1, 0),
                                List.of(1, 1, 1, 0),
                                List.of(0, 0, 1, 0)
                        )
                )
        );
    }
}
