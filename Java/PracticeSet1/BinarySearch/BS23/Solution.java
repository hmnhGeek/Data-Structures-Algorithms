// Problem link - https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
// Solution - https://www.youtube.com/watch?v=SCz-1TtYxDI&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=25


package PracticeSet1.BinarySearch.BS23;

import java.util.List;

public class Solution {
    public static Integer getRowWithMaximumOnes(List<List<Integer>> matrix) {
        /*
            Time complexity is O(n * log(m)) and space complexity is O(1).
         */
        int n = matrix.size(), m = matrix.getFirst().size();
        Integer maxOnes = 0, rowIndex = null;
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = matrix.get(i);
            Integer ones = Utils.getOnesCount(row);
            if (ones > maxOnes) {
                maxOnes = ones;
                rowIndex = i;
            }
        }
        return rowIndex;
    }

    public static void main(String[] args) {

        List<List<Integer>> matrix1 = List.of(
                List.of(0, 0, 1, 1, 1),
                List.of(0, 0, 0, 0, 0),
                List.of(0, 1, 1, 1, 1),
                List.of(0, 0, 0, 0, 0),
                List.of(0, 1, 1, 1, 1)
        );
        System.out.println(Solution.getRowWithMaximumOnes(matrix1));

        List<List<Integer>> matrix2 = List.of(
                List.of(1, 1, 1),
                List.of(0, 0, 1),
                List.of(0, 0, 0)
        );
        System.out.println(Solution.getRowWithMaximumOnes(matrix2));

        List<List<Integer>> matrix3 = List.of(
                List.of(1, 1),
                List.of(1, 1)
        );
        System.out.println(Solution.getRowWithMaximumOnes(matrix3));

        List<List<Integer>> matrix4 = List.of(
                List.of(0, 0, 0),
                List.of(0, 1, 1)
        );
        System.out.println(Solution.getRowWithMaximumOnes(matrix4));

        List<List<Integer>> matrix5 = List.of(
                List.of(0, 0),
                List.of(1, 1),
                List.of(0, 0)
        );
        System.out.println(Solution.getRowWithMaximumOnes(matrix5));

        List<List<Integer>> matrix6 = List.of(
                List.of(0, 1, 1, 1),
                List.of(0, 0, 1, 1),
                List.of(1, 1, 1, 1),
                List.of(0, 0, 0, 0)
        );
        System.out.println(Solution.getRowWithMaximumOnes(matrix6));

        List<List<Integer>> matrix7 = List.of(
                List.of(0, 0, 1, 1),
                List.of(0, 1, 1, 1),
                List.of(0, 0, 1, 1),
                List.of(0, 0, 0, 0)
        );
        System.out.println(Solution.getRowWithMaximumOnes(matrix7));
    }
}
