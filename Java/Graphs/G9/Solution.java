package Graphs.G9;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void floodFill(List<List<Integer>> matrix, Integer startRowIdx, Integer startColIdx, Integer newColor) {
        int n = matrix.size(), m = matrix.getFirst().size();
        if (startRowIdx < 0 || startColIdx < 0 || startRowIdx >= n || startColIdx >= m) return;
        int originalColor = matrix.get(startRowIdx).get(startColIdx);
        List<List<Boolean>> visited = new ArrayList<>();
        getBlankVisitedMatrix(visited, n, m);
        dfs(matrix, startRowIdx, startColIdx, originalColor, newColor, n, m);
        System.out.println(matrix);
    }

    private static void dfs(List<List<Integer>> matrix, Integer startRowIdx, Integer startColIdx, int originalColor, Integer newColor, int n, int m) {
        matrix.get(startRowIdx).set(startColIdx, newColor);
        List<List<Integer>> neighbours = getNeighbours(matrix, startRowIdx, startColIdx, originalColor, n, m);
        for (List<Integer> neighbour : neighbours) {
            int x = neighbour.getFirst(), y = neighbour.getLast();
            dfs(matrix, x, y, originalColor, newColor, n, m);
        }
    }

    private static List<List<Integer>> getNeighbours(List<List<Integer>> matrix, Integer i, Integer j, int originalColor, int n, int m) {
        List<List<Integer>> neighbours = new ArrayList<>();
        if (0 <= i - 1 && i - 1 < n && matrix.get(i - 1).get(j) == originalColor) {
            neighbours.add(Arrays.asList(i - 1, j));
        }
        if (0 <= j + 1 && j + 1 < m && matrix.get(i).get(j + 1) == originalColor) {
            neighbours.add(Arrays.asList(i, j + 1));
        }
        if (0 <= i + 1 && i + 1 < n && matrix.get(i + 1).get(j) == originalColor) {
            neighbours.add(Arrays.asList(i + 1, j));
        }
        if (0 <= j - 1 && j - 1 < m && matrix.get(i).get(j - 1) == originalColor) {
            neighbours.add(Arrays.asList(i, j - 1));
        }
        return neighbours;
    }

    private static void getBlankVisitedMatrix(List<List<Boolean>> visited, int n, int m) {
        for (int i = 0; i < n; i += 1) {
            List<Boolean> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(false);
            }
            visited.add(row);
        }
    }

    public static void main(String[] args) {
        floodFill(
                Arrays.asList(
                        Arrays.asList(1, 1, 1, 0),
                        Arrays.asList(0, 1, 1, 1),
                        Arrays.asList(1, 0, 1, 1)
                ),
                1, 2, 2
        );
    }
}
