package BinarySearch;


import java.util.Arrays;
import java.util.List;

class SolutionBS23 {
    public static Integer getRowIndexWithMax1s(List<List<Integer>> matrix) {
        int n = matrix.size(), m = matrix.getFirst().size();
        int maxCountOf1 = 0;
        int resultantIndex = -1;
        for (int i = 0; i < n; i += 1) {
            int onesCount = getOnesCountBinarySearch(matrix, i, m);
            if (onesCount > maxCountOf1) {
                maxCountOf1 = onesCount;
                resultantIndex = i;
            }
        }
        return resultantIndex;
    }

    private static Integer getOnesCount(List<List<Integer>> matrix, Integer i, Integer m) {
        // This will take O(m) time and O(1) space.
        int onesCount = 0;
        for (int j = 0; j < m; j += 1) {
            if (matrix.get(i).get(j).equals(1)) onesCount += 1;
        }
        return onesCount;
    }

    private static Integer getOnesCountBinarySearch(List<List<Integer>> matrix, Integer i, Integer m) {
        int low = 0, high = m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (matrix.get(i).get(mid).equals(1)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return m - low;
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