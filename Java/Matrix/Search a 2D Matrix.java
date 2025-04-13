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
    }

    public static Cell isPresentInMatrix(List<List<Integer>> matrix, Integer element) {
        int n = matrix.size(), m = matrix.getFirst().size();
        int low = 0, high = n*m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int i = mid/m, j = mid%m;
            if (matrix.get(i).get(j).equals(element)) {
                return new Cell(i, j);
            } else if (matrix.get(i).get(j) > element) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return new Cell(-1, -1);
    }
}