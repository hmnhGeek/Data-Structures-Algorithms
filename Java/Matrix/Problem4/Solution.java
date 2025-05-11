package Matrix.Problem4;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static int getRowIndexWithMax1s(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        int rowIndex = -1;
        int onesCount = 0;
        for (int i = 0; i < n; i += 1) {
            int countOf1 = getOnesCount(mtx, i, 0, m - 1);
            if (countOf1 > onesCount) {
                rowIndex = i;
                onesCount = countOf1;
            }
        }
        return rowIndex;
    }

    private static int getOnesCount(List<List<Integer>> mtx, int i, int low, int high) {
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (mtx.get(i).get(mid).equals(1)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return mtx.getFirst().size() - low;
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
