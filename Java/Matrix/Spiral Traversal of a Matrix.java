// Problem link - https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1

package Matrix;

import java.util.Arrays;
import java.util.List;

enum Direction {
    UP, DOWN, LEFT, RIGHT;
}

class Solution {
    public static void main(String[] args) {
        // Example 1
        List<List<Integer>> matrix = Arrays.asList(
                Arrays.asList(1, 2, 3, 4),
                Arrays.asList(5, 6, 7, 8),
                Arrays.asList(9, 10, 11, 12),
                Arrays.asList(13, 14, 15, 16)
        );
        spiralTraversal(matrix);

        // Example 2
        List<List<Integer>> matrix1 = Arrays.asList(
                Arrays.asList(1, 2, 3, 4, 5, 6),
                Arrays.asList(7, 8, 9, 10, 11, 12),
                Arrays.asList(13, 14, 15, 16, 17, 18)
        );
        spiralTraversal(matrix1);

        // Example 3
        List<List<Integer>> matrix2 = Arrays.asList(
                Arrays.asList(32, 44, 27, 23),
                Arrays.asList(54, 28, 50, 62)
        );
        spiralTraversal(matrix2);
    }

    private static void spiralTraversal(List<List<Integer>> matrix) {
        /*
        * This whole operation will take O(m*n) time and O(m*n) space if we store the traversal.
        * */

        // initialize pointers for the four corners of the matrix
        int n = matrix.size();
        int m = matrix.getFirst().size();
        int top = 0;
        int down = n - 1;
        int left = 0;
        int right = m - 1;

        // set the beginning traversal direction as rightward.
        Direction direction = Direction.RIGHT;

        // while the pointers follow their logical orders
        while (left <= right && top <= down) {
            // if the traversal is to be done from left to right, then it means that the row must be fixed,
            // and we should print from left to right. Once done, the next direction should be downwards in
            // the next iteration. Also, since this row is traversed, increment the `up` pointer.
            if (direction.equals(Direction.RIGHT)) {
                for (int j = left; j <= right; j++) {
                    System.out.print(matrix.get(top).get(j) + " ");
                }
                top += 1;
                direction = Direction.DOWN;
            }
            // if the traversal is to be done from up to down, then it means that the col must be fixed,
            // and we should print from up to down. Once done, the next direction should be leftwards in
            // the next iteration. Also, since this col is traversed, reduce the `right` pointer.
            else if (direction.equals(Direction.DOWN)) {
                for (int i = top; i <= down; i++) {
                    System.out.print(matrix.get(i).get(right) + " ");
                }
                right -= 1;
                direction = Direction.LEFT;
            }
            // if the traversal is to be done from right to left, then it means that the row must be fixed,
            // and we should print from right to left. Once done, the next direction should be upwards in
            // the next iteration. Also, since this row is traversed, reduce the `down` pointer.
            else if (direction.equals(Direction.LEFT)) {
                for (int j = right; j >= left; j--) {
                    System.out.print(matrix.get(down).get(j) + " ");
                }
                down -= 1;
                direction = Direction.UP;
            }
            // if the traversal is to be done from down to up, then it means that the col must be fixed,
            // and we should print from down to up. Once done, the next direction should be rightwards in
            // the next iteration. Also, since this col is traversed, increment the `left` pointer.
            else {
                for (int i = down; i >= top; i--) {
                    System.out.print(matrix.get(i).get(left) + " ");
                }
                left += 1;
                direction = Direction.RIGHT;
            }
        }
        System.out.println();
    }
}