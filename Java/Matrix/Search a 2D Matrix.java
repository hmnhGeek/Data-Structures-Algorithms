// Problem link - https://leetcode.com/problems/search-a-2d-matrix/description/

package Matrix;

import java.util.Arrays;
import java.util.List;

class Cell {
    private Integer rowIndex;
    private Integer colIndex;

    public Cell(Integer i, Integer j) {
        this.rowIndex = i;
        this.colIndex = j;
    }

    public Integer getRowIndex() {
        return rowIndex;
    }

    public void setRowIndex(Integer rowIndex) {
        this.rowIndex = rowIndex;
    }

    public Integer getColIndex() {
        return colIndex;
    }

    public void setColIndex(Integer colIndex) {
        this.colIndex = colIndex;
    }

    @Override
    public String toString() {
        return String.format("(%d, %d)", this.rowIndex, this.colIndex);
    }
}

class Problem2 {
    public static void main(String[] args) {
        // Example 1
        List<List<Integer>> matrix1 = Arrays.asList(
                Arrays.asList(1, 3, 5, 7),
                Arrays.asList(10, 11, 16, 20),
                Arrays.asList(23, 30, 34, 60)
        );
        System.out.println(isPresentInMatrix(matrix1, 3));

        // Example 2
        System.out.println(isPresentInMatrix(matrix1, 13));

        // Example 3
        List<List<Integer>> matrix2 = Arrays.asList(
                Arrays.asList(1, 2, 3, 4),
                Arrays.asList(5, 6, 7, 8),
                Arrays.asList(9, 10, 11, 12)
        );
        System.out.println(isPresentInMatrix(matrix2, 8));

        // Example 4
        List<List<Integer>> matrix3 = Arrays.asList(
                Arrays.asList(1, 2, 4),
                Arrays.asList(6, 7, 8),
                Arrays.asList(9, 10, 34)
        );
        System.out.println(isPresentInMatrix(matrix3, 78));
    }

    public static Cell isPresentInMatrix(List<List<Integer>> matrix, Integer element) {
        /**
         * Time complexity is O(log(n) + log(m)) and space complexity is O(1).
         */

        // define the dimensions of the matrix
        int n = matrix.size(), m = matrix.getFirst().size();

        // define the search space of the binary search.
        int low = 0, high = n*m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);

            // get the cell index using mid.
            int i = mid/m, j = mid%m;

            // if the element at this cell is same as requested element.
            if (matrix.get(i).get(j).equals(element)) {
                return new Cell(i, j);
            } else if (matrix.get(i).get(j) > element) {
                // if mtx[i][j] > element, we must search on left.
                high = mid - 1;
            } else {
                // else search on right.
                low = mid + 1;
            }
        }

        // else the element is not found.
        return new Cell(-1, -1);
    }
}