// Problem link - https://www.geeksforgeeks.org/problems/sorted-matrix2333/1


package Matrix.Problem5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        sortMatrix(
                Arrays.asList(
                        Arrays.asList(10,20,30,40),
                        Arrays.asList(15,25,35,45),
                        Arrays.asList(27,29,37,48),
                        Arrays.asList(32,33,39,50)
                )
        );

        sortMatrix(
                Arrays.asList(
                        Arrays.asList(1, 5, 3),
                        Arrays.asList(2, 8, 7),
                        Arrays.asList(4, 6, 9)
                )
        );
    }

    public static void sortMatrix(List<List<Integer>> matrix) {
        /*
            Time complexity is O(n^2 * log(n)) and space complexity is O(n^2).
         */

        // This takes O(n^2) time and O(n^2) space.
        List<Integer> array = flatten(matrix);

        // This takes O(n^2 * log(n)) time.
        QuickSort.sort(array);

        // This takes another O(n^2) time.
        buildBackMatrix(matrix, array);
        System.out.println(matrix);
    }

    private static void buildBackMatrix(List<List<Integer>> matrix, List<Integer> array) {
        int counter = 0;
        int n = matrix.size(), m = matrix.getFirst().size();
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                matrix.get(i).set(j, array.get(counter));
                counter += 1;
            }
        }
    }

    private static List<Integer> flatten(List<List<Integer>> matrix) {
        int n = matrix.size(), m = matrix.getFirst().size();
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                result.add(matrix.get(i).get(j));
            }
        }
        return result;
    }
}
