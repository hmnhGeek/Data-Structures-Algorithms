package DynamicProgramming.DP7;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is O(3^n) and space complexity is O(n).
     */
    public static Integer getMaxPoints(List<List<Integer>> matrix) {
        int n = matrix.size();
        return Math.max(
                solve(matrix, n - 1, 2),
                Math.max(
                    solve(matrix, n - 1, 0),
                    solve(matrix, n - 1, 1)
                )
        );
    }

    private static Integer solve(List<List<Integer>> matrix, int i, int j) {
        if (i == 0) return matrix.getFirst().get(j);
        List<Integer> nextIndices = Utils.getNext(j);
        Integer result = Integer.MIN_VALUE;
        for (int index : nextIndices) {
            result = Math.max(result, matrix.get(i).get(j) + solve(matrix, i - 1, index));
        }
        return result;
    }
}
