package PracticeSet1.Matrix.Problem2;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static boolean getElementFromMatrix(List<List<Integer>> mtx, Integer x) {
        int n = mtx.size(), m = mtx.getFirst().size();
        int low = 0;
        int high = n*m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int row = mid / m, col = mid % m;
            if (mtx.get(row).get(col) == x) {
                return true;
            }
            if (mtx.get(row).get(col) > x) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(
                getElementFromMatrix(
                        Arrays.asList(
                                Arrays.asList(1, 3, 5, 7),
                                Arrays.asList(10, 11, 16, 20),
                                Arrays.asList(23, 30, 34, 60)
                        ),
                        3
                )
        );

        System.out.println(
                getElementFromMatrix(
                        Arrays.asList(
                                Arrays.asList(1, 3, 5, 7),
                                Arrays.asList(10, 11, 16, 20),
                                Arrays.asList(23, 30, 34, 60)
                        ),
                        13
                )
        );
    }
}
