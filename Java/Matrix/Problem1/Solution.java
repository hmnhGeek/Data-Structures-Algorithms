// Problem link - https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1


package Matrix.Problem1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                getSpiralTraversal(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3, 4, 5, 6),
                                Arrays.asList(7, 8, 9, 10, 11, 12),
                                Arrays.asList(13, 14, 15, 16, 17, 18)
                        )
                )
        );

        System.out.println(
                getSpiralTraversal(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3, 4),
                                Arrays.asList(5, 6, 7, 8),
                                Arrays.asList(9, 10, 11, 12),
                                Arrays.asList(13, 14, 15, 16)
                        )
                )
        );

        System.out.println(
                getSpiralTraversal(
                        Arrays.asList(
                                Arrays.asList(32, 44, 27, 23),
                                Arrays.asList(54, 28, 50, 62)
                        )
                )
        );
    }

    public static List<Integer> getSpiralTraversal(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm) and space complexity is O(mn).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        int left = 0, right = m - 1, top = 0, down = n - 1;
        String direction = "R";
        List<Integer> result = new ArrayList<>();
        while (top <= down) {
            if (direction == "R") {
                for (int i = left; i <= right; i += 1) {
                    result.add(mtx.get(top).get(i));
                }
                top += 1;
                direction = "D";
            } else if (direction == "D") {
                for (int i = top; i <= down; i += 1) {
                    result.add(mtx.get(i).get(right));
                }
                right -= 1;
                direction = "L";
            } else if (direction == "L") {
                for (int i = right; i >= left; i -= 1) {
                    result.add(mtx.get(down).get(i));
                }
                down -= 1;
                direction = "U";
            } else {
                for (int i = down; i >= top; i -= 1) {
                    result.add(mtx.get(i).get(left));
                }
                left += 1;
                direction = "R";
            }
        }
        return result;
    }
}
