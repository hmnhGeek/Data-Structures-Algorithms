// Problem link - https://www.spoj.com/problems/ANARC05B/

package SearchingAndSorting.Problem32;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        # The recursion stack will take O(path length + space of dp array) space, i.e., O(N + 2N) = O(N)
        # (assuming same length of both the arrays in worst case). The time complexity would
        # be O(N * log(N)) where in at each cell we have two options, but because of overlapping sub-problems, we can
        # reduce this from 2^N to N.
     */
    public static Integer doubleHelix(List<Integer> a, List<Integer> b) {
        List<List<Integer>> matrix = List.of(a, b);
        Integer n = a.size(), m = b.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < 2; i += 1) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int j = 0; j < Math.max(n, m); j += 1) {
                map.put(j, null);
            }
            dp.put(i, map);
        }
        return Math.max(solve(matrix, 0, 0, n, m, dp), solve(matrix, 1, 0, n, m, dp));
    }

    private static Integer solve(List<List<Integer>> matrix, int i, int j, Integer n, Integer m, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == 0 && j == n) return 0;
        if (i == 1 && j == m) return 0;
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        Integer element = matrix.get(i).get(j);
        Integer j0 = getIndexInOtherArray(matrix, getComplementary(i), element);
        Integer left = element + solve(matrix, i, j + 1, n, m, dp);
        Integer right = Integer.MIN_VALUE;
        if (j0 != -1) {
            right = element + solve(matrix, getComplementary(i), j0 + 1, n, m, dp);
        }
        dp.get(i).put(j, Math.max(left, right));
        return dp.get(i).get(j);
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
