// Problem link - https://www.geeksforgeeks.org/problems/sorted-matrix2333/1

package PracticeSet1.Matrix.Problem5;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(sortMatrix(
                Arrays.asList(
                        Arrays.asList(10,20,30,40),
                        Arrays.asList(15,25,35,45),
                        Arrays.asList(27,29,37,48),
                        Arrays.asList(32,33,39,50)
                )
        ));

        System.out.println(sortMatrix(
                Arrays.asList(
                        Arrays.asList(1, 5, 3),
                        Arrays.asList(2, 8, 7),
                        Arrays.asList(4, 6, 9)
                )
        ));
    }

    public static List<List<Integer>> sortMatrix(List<List<Integer>> matrix) {
        /*
            Time complexity is O(n^2 * log(n)) time and O(n^2) space.
         */

        if (matrix == null || matrix.isEmpty()) return null;
        int n = matrix.size();

        // O(n^2) time and O(n^2) space.
        List<Integer> flattenedMatrix = Utility.flattenMatrix(matrix);

        // O(n^2 * log(n)) time
        Utility.quickSort(flattenedMatrix);

        // O(n^2) time and O(n^2) space.
        return Utility.rebuildMatrix(flattenedMatrix, n);
    }
}
