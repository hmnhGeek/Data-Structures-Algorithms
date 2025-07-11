package Matrix.Problem8;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static <T> void rotateMatrix(List<List<T>> mtx) {
        Utils.transpose(mtx);
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
    }
}
