// Problem link - https://www.geeksforgeeks.org/dsa/given-matrix-o-x-replace-o-x-surrounded-x/
// Solution - https://www.youtube.com/watch?v=BtdgAys4yMk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=14


package Graphs.G14;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<List<Character>> m1 = Arrays.asList(
                Arrays.asList('X','X','X','X'),
                Arrays.asList('X', 'O', 'O', 'X'),
                Arrays.asList('X','X','O','X'),
                Arrays.asList('X','O','X','X')
        );
        surroundRegions(m1);
        System.out.println(m1);

        List<List<Character>> m2 = Arrays.asList(Arrays.asList('X'));
        surroundRegions(m2);
        System.out.println(m2);

        List<List<Character>> m3 = Arrays.asList(
                Arrays.asList('X', 'O', 'X', 'X', 'X', 'X'),
                Arrays.asList('X', 'O', 'X', 'X', 'O', 'X'),
                Arrays.asList('X', 'X', 'X', 'O', 'O', 'X'),
                Arrays.asList('O', 'X', 'X', 'X', 'X', 'X'),
                Arrays.asList('X', 'X', 'X', 'O', 'X', 'O'),
                Arrays.asList('O', 'O', 'X', 'O', 'O', 'O')
        );
        surroundRegions(m3);
        System.out.println(m3);

        List<List<Character>> m4 = Arrays.asList(
                Arrays.asList('X', 'X', 'X', 'X'),
                Arrays.asList('X', 'O', 'X', 'X'),
                Arrays.asList('X', 'O', 'O', 'X'),
                Arrays.asList('X', 'O', 'X', 'X'),
                Arrays.asList('X', 'X', 'O', 'O')
        );
        surroundRegions(m4);
        System.out.println(m4);
    }

    public static void surroundRegions(List<List<Character>> mtx) {
        /*
            Time complexity is O(nm) and space complexity is O(nm).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        List<List<Boolean>> visited = getVisited(n, m);
        for (int j = 0; j < m - 1; j += 1) {
            if (mtx.getFirst().get(j).equals('O')) {
                dfs(mtx, 0, j, n, m, visited);
            }
        }
        for (int i = 0; i < n - 1; i += 1) {
            if (mtx.get(i).getLast().equals('O')) {
                dfs(mtx, i, m - 1, n, m, visited);
            }
        }
        for (int j = m - 1; j > 0; j -= 1) {
            if (mtx.getLast().get(j).equals('O')) {
                dfs(mtx, n - 1, j, n, m, visited);
            }
        }
        for (int i = n - 1; i > 0; i -= 1) {
            if (mtx.get(i).getFirst().equals('O')) {
                dfs(mtx, i, 0, n, m, visited);
            }
        }
        convertOsToXs(mtx, n, m);
        convertZsBackToOs(mtx, n, m);
    }

    private static void convertZsBackToOs(List<List<Character>> mtx, int n, int m) {
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (mtx.get(i).get(j).equals('Z')) {
                    mtx.get(i).set(j, 'O');
                }
            }
        }
    }

    private static void convertOsToXs(List<List<Character>> mtx, int n, int m) {
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (mtx.get(i).get(j).equals('O')) {
                    mtx.get(i).set(j, 'X');
                }
            }
        }
    }

    private static void dfs(List<List<Character>> mtx, int i, int j, int n, int m, List<List<Boolean>> visited) {
        visited.get(i).set(j, true);
        mtx.get(i).set(j, 'Z');
        List<List<Integer>> neighbours = getNeighbours(mtx, i, j, n, m, visited);
        for (List<Integer> neighbour : neighbours) {
            if (!visited.get(neighbour.getFirst()).get(neighbour.getLast())) {
                dfs(mtx, neighbour.getFirst(), neighbour.getLast(), n, m, visited);
            }
        }
    }

    private static List<List<Integer>> getNeighbours(List<List<Character>> mtx, int i, int j, int n, int m, List<List<Boolean>> visited) {
        List<List<Integer>> result = new ArrayList<>();
        if (0 <= i - 1 && i - 1 < n && !visited.get(i - 1).get(j) && mtx.get(i - 1).get(j).equals('O')) {
            result.add(List.of(i - 1, j));
        }
        if (0 <= j + 1 && j + 1 < m && !visited.get(i).get(j + 1) && mtx.get(i).get(j + 1).equals('O')) {
            result.add(List.of(i, j + 1));
        }
        if (0 <= i + 1 && i + 1 < n && !visited.get(i + 1).get(j) && mtx.get(i + 1).get(j).equals('O')) {
            result.add(List.of(i + 1, j));
        }
        if (0 <= j - 1 && j - 1 < m && !visited.get(i).get(j - 1) && mtx.get(i).get(j - 1).equals('O')) {
            result.add(List.of(i, j - 1));
        }
        return result;
    }

    private static List<List<Boolean>> getVisited(int n, int m) {
        List<List<Boolean>> visited = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Boolean> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(false);
            }
            visited.add(row);
        }
        return visited;
    }
}
