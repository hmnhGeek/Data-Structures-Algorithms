package PracticeSet1.Matrix.Problem8;

import java.util.Arrays;
import java.util.List;

public class Solution {
    private static void transpose(List<List<Integer>> mtx) {
        int n = mtx.size();
        for (int i = 0; i < n; i += 1) {
            for (int j = i; j < n; j += 1) {
                int temp = mtx.get(i).get(j);
                mtx.get(i).set(j, mtx.get(j).get(i));
                mtx.get(j).set(i, temp);
            }
        }
    }

    private static void reverseRows(List<List<Integer>> mtx) {
        int n = mtx.size();
        for (int i = 0; i < n; i += 1) {
            mtx.set(i, mtx.get(i).reversed());
        }
    }

    public static void rotate(List<List<Integer>> mtx) {
        transpose(mtx);
        reverseRows(mtx);
        System.out.println(mtx);
    }

    public static void main(String[] args) {
        rotate(
                Arrays.asList(
                        Arrays.asList(1, 2, 3),
                        Arrays.asList(4, 5, 6),
                        Arrays.asList(7, 8, 9)
                )
        );

        rotate(
                Arrays.asList(
                        Arrays.asList(1, 2, 3, 4),
                        Arrays.asList(5, 6, 7, 8),
                        Arrays.asList(9, 10, 11, 12),
                        Arrays.asList(13, 14, 15, 16)
                )
        );
    }
}
