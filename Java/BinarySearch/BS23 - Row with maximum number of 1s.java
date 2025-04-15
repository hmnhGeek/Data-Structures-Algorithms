package BinarySearch;


import java.util.Arrays;
import java.util.List;

class SolutionBS23 {
    public static Integer getRowIndexWithMax1s(List<List<Integer>> matrix) {
        int n = matrix.size(), m = matrix.getFirst().size();
        int maxCountOf1 = 0;
        int resultantIndex = -1;
        for (int i = 0; i < n; i += 1) {
            int onesCount = getOnesCount(matrix, i, m);
            if (onesCount > maxCountOf1) {
                maxCountOf1 = onesCount;
                resultantIndex = i;
            }
        }
        return resultantIndex;
    }

    private static Integer getOnesCount(List<List<Integer>> matrix, Integer i, Integer m) {
        int onesCount = 0;
        for (int j = 0; j < m; j += 1) {
            if (matrix.get(i).get(j).equals(1)) onesCount += 1;
        }
        return onesCount;
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
    }
}