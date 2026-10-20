// Problem link - https://www.geeksforgeeks.org/dsa/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/


package PracticeSet2.Matrix.Problem8;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void rotateMtx(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm) and space complexity is O(1).
         */
        System.out.println("Matrix Before: ");
        System.out.println(mtx);
        transposeMtx(mtx);
        lateralInvert(mtx);
        System.out.println("Matrix After: ");
        System.out.println(mtx);
    }

    private static void lateralInvert(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        for (int i = 0; i < n; i += 1) {
            int a = 0, b = m - 1;
            while (a < b) {
                Integer temp = mtx.get(i).get(b);
                mtx.get(i).set(b, mtx.get(i).get(a));
                mtx.get(i).set(a, temp);
                a += 1;
                b -= 1;
            }
        }
    }

    private static void transposeMtx(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        for (int i = 0; i < n; i += 1) {
            for (int j = m - 1; j > i; j -= 1) {
                Integer temp = mtx.get(i).get(j);
                mtx.get(i).set(j, mtx.get(j).get(i));
                mtx.get(j).set(i, temp);
            }
        }
    }

    public static void main(String[] args) {
        rotateMtx(
                Arrays.asList(
                        Arrays.asList(1, 2, 3),
                        Arrays.asList(4, 5, 6),
                        Arrays.asList(7, 8, 9)
                )
        );

        rotateMtx(
                Arrays.asList(
                        Arrays.asList(1, 2, 3, 4),
                        Arrays.asList(5, 6, 7, 8),
                        Arrays.asList(9, 10, 11, 12),
                        Arrays.asList(13, 14, 15, 16)
                )
        );
    }
}
