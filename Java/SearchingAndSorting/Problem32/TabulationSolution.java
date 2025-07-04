// Problem link - https://www.spoj.com/problems/ANARC05B/

package SearchingAndSorting.Problem32;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        # The time complexity still remains O(N * log(N)) but space complexity reduces to just O(2N) = O(N) with no
        # recursion calls.
     */
    public static Integer doubleHelix(List<Integer> a, List<Integer> b) {
        List<List<Integer>> matrix = List.of(a, b);
        Integer n = a.size(), m = b.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < 2; i += 1) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int j = 0; j <= Math.max(n, m); j += 1) {
                map.put(j, Integer.MIN_VALUE);
            }
            dp.put(i, map);
        }
        dp.get(0).put(n, 0);
        dp.get(1).put(m, 0);

        // This O(2N) loop will run for the case when we assume to start from row = 0 (first array).
        for (int i = 0; i < 2; i += 1) {
            for (int j = matrix.get(i).size() - 1; j >= 0; j -= 1) {
                Integer element = matrix.get(i).get(j);
                Integer j0 = getIndexInOtherArray(matrix, getComplementary(i), element);
                Integer left = element + dp.get(i).get(j + 1);
                Integer right = Integer.MIN_VALUE;
                if (j0 != -1) {
                    right = element + dp.get(getComplementary(i)).get(j0 + 1);
                }
                dp.get(i).put(j, Math.max(left, right));
            }
        }

        // This O(2N) loop will run for the case when we assume to start from row = 1 (second array).
        for (int i = 1; i >= 0; i -= 1) {
            for (int j = matrix.get(i).size() - 1; j >= 0; j -= 1) {
                Integer element = matrix.get(i).get(j);
                Integer j0 = getIndexInOtherArray(matrix, getComplementary(i), element);
                Integer left = element + dp.get(i).get(j + 1);
                Integer right = Integer.MIN_VALUE;
                if (j0 != -1) {
                    right = element + dp.get(getComplementary(i)).get(j0 + 1);
                }
                dp.get(i).put(j, Math.max(left, right));
            }
        }

        // return the result.
        return Math.max(dp.get(0).get(0), dp.get(1).get(0));
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
