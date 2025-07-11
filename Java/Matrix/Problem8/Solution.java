// Problem link - https://www.geeksforgeeks.org/dsa/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/

package Matrix.Problem8;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static <T> void rotateMatrix(List<List<T>> mtx) {
        /*
            Overall time complexity is O(n^2) and space complexity is O(1).
         */

        // this operation will take O(n^2) time complexity and O(1) space.
        Utils.transpose(mtx);

        // This will also take O(n^2) time and O(1) space.
        Utils.lateralInvert(mtx);
    }

    public static void main(String[] args) {
        // Example 1
        List<List<Integer>> mtx1 = Arrays.asList(
                Arrays.asList(1, 2, 3),
                Arrays.asList(4, 5, 6),
                Arrays.asList(7, 8, 9)
        );
        rotateMatrix(mtx1);
        System.out.println(mtx1);

        // Example 2
        List<List<Integer>> mtx2 = Arrays.asList(
                Arrays.asList(1, 2, 3, 4),
                Arrays.asList(5, 6, 7, 8),
                Arrays.asList(9, 10, 11, 12),
                Arrays.asList(13, 14, 15, 16)
        );
        rotateMatrix(mtx2);
        System.out.println(mtx2);
    }
}
