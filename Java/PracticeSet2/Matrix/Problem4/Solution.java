// Problem link - https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
// Solution - https://www.youtube.com/watch?v=SCz-1TtYxDI&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=25


package PracticeSet2.Matrix.Problem4;

import java.util.Arrays;
import java.util.List;

public class Solution {
    private static Integer getCountOfOnes(List<Integer> arr) {
        int n = arr.size();
        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid).equals(0)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return n - low;
    }

    public static Integer getRowIndexWithMax1s(List<List<Integer>> mtx) {
        /*
            Time complexity is O(n * log(m)) and space complexity is O(1).
         */
        int rowIndex = -1;
        int maxOnes = 0;
        for (int i = 0; i < mtx.size(); i += 1) {
            int onesCount = getCountOfOnes(mtx.get(i));
            if (onesCount > maxOnes) {
                maxOnes = onesCount;
                rowIndex = i;
            }
        }
        return rowIndex;
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
