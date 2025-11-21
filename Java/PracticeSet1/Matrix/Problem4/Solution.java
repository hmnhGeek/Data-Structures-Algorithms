// Problem link - https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
// Solution - https://www.youtube.com/watch?v=SCz-1TtYxDI&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=25


package PracticeSet1.Matrix.Problem4;

import java.util.Arrays;
import java.util.List;

public class Solution {
    private static int getCountOfOnes(List<Integer> arr, Integer m) {
        /*
            Time complexity is O(log(m)) and space complexity is O(1).
         */
        int low = 0, high = m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) == 1) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return m - low;
    }

    public static int getRowIndexWithMax1s(List<List<Integer>> mtx) {
        /*
            Time complexity is O(n * log(m)) and space complexity is O(1).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        int maxOnes = 0, row = -1;
        for (int i = 0; i < n; i += 1) {
            int countOfOnes = getCountOfOnes(mtx.get(i), m);
            if (maxOnes < countOfOnes) {
                maxOnes = countOfOnes;
                row = i;
            }
        }
        return row;
    }

    public static void main(String[] args) {
        List<List<Integer>> matrix1 = Arrays.asList(
                Arrays.asList(0, 0, 1, 1, 1),
                Arrays.asList(0, 0, 0, 0, 0),
                Arrays.asList(0, 1, 1, 1, 1),
                Arrays.asList(0, 0, 0, 0, 0),
                Arrays.asList(0, 1, 1, 1, 1)
        );
        System.out.println(getRowIndexWithMax1s(matrix1));

        List<List<Integer>> matrix2 = Arrays.asList(
                Arrays.asList(1, 1, 1),
                Arrays.asList(0, 0, 1),
                Arrays.asList(0, 0, 0)
        );
        System.out.println(getRowIndexWithMax1s(matrix2));

        List<List<Integer>> matrix3 = Arrays.asList(
                Arrays.asList(1, 1),
                Arrays.asList(1, 1)
        );
        System.out.println(getRowIndexWithMax1s(matrix3));

        List<List<Integer>> matrix4 = Arrays.asList(
                Arrays.asList(0, 0, 0),
                Arrays.asList(0, 1, 1)
        );
        System.out.println(getRowIndexWithMax1s(matrix4));

        List<List<Integer>> matrix5 = Arrays.asList(
                Arrays.asList(0, 0),
                Arrays.asList(1, 1),
                Arrays.asList(0, 0)
        );
        System.out.println(getRowIndexWithMax1s(matrix5));

        List<List<Integer>> matrix6 = Arrays.asList(
                Arrays.asList(0, 1, 1, 1),
                Arrays.asList(0, 0, 1, 1),
                Arrays.asList(1, 1, 1, 1),
                Arrays.asList(0, 0, 0, 0)
        );
        System.out.println(getRowIndexWithMax1s(matrix6));

        List<List<Integer>> matrix7 = Arrays.asList(
                Arrays.asList(0, 0, 1, 1),
                Arrays.asList(0, 1, 1, 1),
                Arrays.asList(0, 0, 1, 1),
                Arrays.asList(0, 0, 0, 0)
        );
        System.out.println(getRowIndexWithMax1s(matrix7));
    }
}
