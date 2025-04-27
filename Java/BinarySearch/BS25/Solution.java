// Problem link - https://leetcode.com/problems/search-a-2d-matrix-ii/
// Solution - https://www.youtube.com/watch?v=9ZbB397jU4k&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=27

package BinarySearch.BS25;

import java.util.List;

class Cell {
    private final Integer x;
    private final Integer y;

    public Cell(Integer x, Integer y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return String.format("(%d, %d)", this.x, this.y);
    }
}

public class Solution {
    public static Cell search(List<List<Integer>> matrix, Integer element) {
        /*
            Time complexity is O(m + n) and space complexity is O(1).
         */

        int n = matrix.size(), m = matrix.getFirst().size();
        int row = 0, col = m - 1;
        while (row < n && col >= 0) {
            if (matrix.get(row).get(col).equals(element)) {
                return new Cell(row, col);
            } else if (element < matrix.get(row).get(col)) {
                col -= 1;
            } else {
                row += 1;
            }
        }
        return new Cell(-1, -1);
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.search(
                        List.of(
                                List.of(1, 4, 7, 11, 15),
                                List.of(2, 5, 8, 12, 19),
                                List.of(3, 6, 9, 16, 22),
                                List.of(10, 13, 14, 17, 24),
                                List.of(18, 21, 23, 26, 30)
                        ),
                        14
                )
        );

        System.out.println(
                Solution.search(
                        List.of(
                                List.of(1, 4, 7, 11, 15),
                                List.of(2, 5, 8, 12, 19),
                                List.of(3, 6, 9, 16, 22),
                                List.of(10, 13, 14, 17, 24),
                                List.of(18, 21, 23, 26, 30)
                        ),
                        5
                )
        );

        System.out.println(
                Solution.search(
                        List.of(
                                List.of(1, 4, 7, 11, 15),
                                List.of(2, 5, 8, 12, 19),
                                List.of(3, 6, 9, 16, 22),
                                List.of(10, 13, 14, 17, 24),
                                List.of(18, 21, 23, 26, 30)
                        ),
                        20
                )
        );

        System.out.println(
                Solution.search(
                        List.of(
                                List.of(1, 2, 4, 5),
                                List.of(3, 4, 9, 16),
                                List.of(7, 10, 14, 29)
                        ),
                        8
                )
        );

        System.out.println(
                Solution.search(
                        List.of(
                                List.of(1, 2, 3),
                                List.of(4, 5, 6),
                                List.of(7, 8, 9)
                        ),
                        5
                )
        );
    }
}
