package BinarySearch.BS24;

import java.util.Arrays;
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
        Integer n = matrix.size(), m = matrix.getFirst().size();
        Integer low = 0, high = n*m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int x = mid/m, y = mid%m;
            if (matrix.get(x).get(y).equals(element)) {
                return new Cell(x, y);
            } else if (matrix.get(x).get(y) > element) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return new Cell(-1, -1);
    }

    public static void main(String[] args) {
        System.out.println(
                search(
                        Arrays.asList(
                                Arrays.asList(3, 4, 7, 9),
                                Arrays.asList(12, 13, 16, 18),
                                Arrays.asList(20, 21, 23, 29)
                        ), 23
                )
        );

        System.out.println(
                search(
                        Arrays.asList(
                                Arrays.asList(1, 3, 5, 7),
                                Arrays.asList(10, 11, 16, 20),
                                Arrays.asList(23, 30, 34, 60)
                        ), 3
                )
        );

        System.out.println(
                search(
                        Arrays.asList(
                                Arrays.asList(1, 3, 5, 7),
                                Arrays.asList(10, 11, 16, 20),
                                Arrays.asList(23, 30, 34, 60)
                        ), 13
                )
        );

        System.out.println(
                search(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3, 4),
                                Arrays.asList(5, 6, 7, 8),
                                Arrays.asList(9, 10, 11, 12)
                        ), 8
                )
        );
    }
}
