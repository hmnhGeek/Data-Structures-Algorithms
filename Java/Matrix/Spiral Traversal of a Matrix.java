package Matrix;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

enum Direction {
    UP, DOWN, LEFT, RIGHT;
}

class Solution {
    public static void main(String[] args) {
        List<List<Integer>> matrix = Arrays.asList(
                Arrays.asList(1, 2, 3, 4),
                Arrays.asList(5, 6, 7, 8),
                Arrays.asList(9, 10, 11, 12),
                Arrays.asList(13, 14, 15, 16)
        );
        spiralTraversal(matrix);
    }

    private static void spiralTraversal(List<List<Integer>> matrix) {
        int n = matrix.size();
        int m = matrix.getFirst().size();
        int top = 0;
        int down = n - 1;
        int left = 0;
        int right = m - 1;
        Direction direction = Direction.RIGHT;
        while (left <= right && top <= down) {
            if (direction.equals(Direction.RIGHT)) {
                for (int j = left; j <= right; j++) {
                    System.out.print(matrix.get(top).get(j) + " ");
                }
                top += 1;
                direction = Direction.DOWN;
            } else if (direction.equals(Direction.DOWN)) {
                for (int i = top; i <= down; i++) {
                    System.out.print(matrix.get(i).get(right) + " ");
                }
                right -= 1;
                direction = Direction.LEFT;
            } else if (direction.equals(Direction.LEFT)) {
                for (int j = right; j >= left; j--) {
                    System.out.print(matrix.get(down).get(j) + " ");
                }
                down -= 1;
                direction = Direction.UP;
            } else {
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