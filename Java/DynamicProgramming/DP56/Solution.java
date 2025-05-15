// Problem link - https://www.naukri.com/code360/problems/count-square-submatrices-with-all-ones_3751502?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=auS1fynpnjo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=57

package DynamicProgramming.DP56;

import java.util.ArrayList;
import java.util.List;

public class Solution {

    // Function to count the number of square submatrices filled with 1s
    public static Integer countSquareSubMatrices(List<List<Integer>> matrix) {
        /*
            Time complexity is O(mn) and space complexity is O(mn).
         */

        int n = matrix.size(), m = matrix.getFirst().size();

        // Initialize the DP matrix with first row and first column values handled
        List<List<Integer>> dp = getDpMatrix(matrix);

        // Fill the dp matrix using dynamic programming
        for (int i = 1; i < n; i += 1) {
            for (int j = 1; j < m; j += 1) {
                if (matrix.get(i).get(j).equals(0)) {
                    // If the current cell in the input matrix is 0, it can't be part of any square
                    dp.get(i).set(j, 0);
                } else {
                    // Update current cell in dp matrix with 1 plus the minimum of
                    // top, left, and top-left neighbors
                    dp.get(i).set(j, 1 + Math.min(
                            dp.get(i - 1).get(j),
                            Math.min(dp.get(i - 1).get(j - 1), dp.get(i).get(j - 1))
                    ));
                }
            }
        }

        // Sum up all values in the dp matrix to get the total number of square submatrices
        Integer sum = 0;
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                sum += dp.get(i).get(j);
            }
        }

        return sum;
    }

    // Helper function to initialize the dp matrix with the first row and first column
    private static List<List<Integer>> getDpMatrix(List<List<Integer>> matrix) {
        int n = matrix.size(), m = matrix.getFirst().size();
        List<List<Integer>> dp = new ArrayList<>();

        // First row initialization: copy the first row from the input matrix
        List<Integer> row = new ArrayList<>();
        for (int j = 0; j < m; j += 1) {
            row.add(matrix.getFirst().get(j));
        }
        dp.add(row);

        // Initialize remaining rows
        for (int i = 1; i < n; i += 1) {
            List<Integer> r = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                if (j == 0) {
                    // First column: directly copy value from input matrix
                    r.add(matrix.get(i).getFirst());
                } else {
                    // Other cells in the row: initialize to 0 for now
                    r.add(0);
                }
            }
            dp.add(r);
        }

        return dp;
    }

    // Main method to test the countSquareSubMatrices function with sample inputs
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
