package SearchingAndSorting.Problem32;

import java.util.Arrays;
import java.util.List;

public class RecursiveSolution {
    public static Integer doubleHelix(List<Integer> a, List<Integer> b) {
        List<List<Integer>> matrix = List.of(a, b);
        Integer n = a.size(), m = b.size();
        return Math.max(solve(matrix, 0, 0, n, m), solve(matrix, 1, 0, n, m));
    }

    private static Integer solve(List<List<Integer>> matrix, int i, int j, Integer n, Integer m) {
        if (i == 0 && j == n) return 0;
        if (i == 1 && j == m) return 0;
        Integer element = matrix.get(i).get(j);
        Integer j0 = getIndexInOtherArray(matrix, getComplementary(i), element);
        Integer left = element + solve(matrix, i, j + 1, n, m);
        Integer right = Integer.MIN_VALUE;
        if (j0 != -1) {
            right = element + solve(matrix, getComplementary(i), j0 + 1, n, m);
        }
        return Math.max(left, right);
    }

    private static Integer getIndexInOtherArray(List<List<Integer>> matrix, int complementary, Integer element) {
        return binarySearch(matrix.get(complementary), element);
    }

    private static Integer binarySearch(List<Integer> arr, Integer element) {
        int n = arr.size();
        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            Integer x = arr.get(mid);
            if (x.equals(element)) {
                return mid;
            } else if (x < element) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

    private static int getComplementary(int i) {
        if (i == 0) return 1;
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(doubleHelix(Arrays.asList(-5, 100, 1000, 1005), Arrays.asList(-12, 1000, 1001)));
        System.out.println(
                doubleHelix(
                        Arrays.asList(3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62),
                        Arrays.asList(1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100)
                )
        );
        System.out.println(
                doubleHelix(
                        Arrays.asList(0, 2, 6, 7, 8, 9),
                        Arrays.asList(0, 2, 4, 5, 7, 9)
                )
        );
    }
}
