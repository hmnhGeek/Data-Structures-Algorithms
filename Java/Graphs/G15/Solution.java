package Graphs.G15;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                getCountOfEnclaves(
                        Arrays.asList(
                                Arrays.asList(0, 0, 0, 0),
                                Arrays.asList(1, 0, 1, 0),
                                Arrays.asList(0, 1, 1, 0),
                                Arrays.asList(0, 0, 0, 0)
                        )
                )
        );

        System.out.println(
                getCountOfEnclaves(
                        Arrays.asList(
                                Arrays.asList(0, 1, 1, 0),
                                Arrays.asList(0, 0, 1, 0),
                                Arrays.asList(0, 0, 1, 0),
                                Arrays.asList(0, 0, 0, 0)
                        )
                )
        );

        System.out.println(
                getCountOfEnclaves(
                        Arrays.asList(
                                Arrays.asList(0, 0, 0, 1),
                                Arrays.asList(0, 1, 1, 0),
                                Arrays.asList(0, 1, 1, 0),
                                Arrays.asList(0, 0, 0, 1),
                                Arrays.asList(0, 1, 1, 0)
                        )
                )
        );
    }

    private static List<List<Integer>> getValidNeighbours(List<List<Integer>> graph, Integer i, Integer j, Integer n, Integer m) {
        List<List<Integer>> neighbours = new ArrayList<>();
        if (0 <= i - 1 && i - 1 < n && graph.get(i - 1).get(j).equals(1)) {
            neighbours.add(List.of(i - 1, j));
        }
        if (0 <= j + 1 && j + 1 < m && graph.get(i).get(j + 1).equals(1)) {
            neighbours.add(List.of(i, j + 1));
        }
        if (0 <= i + 1 && i + 1 < n && graph.get(i + 1).get(j).equals(1)) {
            neighbours.add(List.of(i + 1, j));
        }
        if (0 <= j - 1 && j - 1 < m && graph.get(i).get(j - 1).equals(1)) {
            neighbours.add(List.of(i, j - 1));
        }
        return neighbours;
    }

    private static void dfs(List<List<Integer>> graph, Integer i, Integer j, Integer n, Integer m) {
        graph.get(i).set(j, 2);
        List<List<Integer>> neighbours = Solution.getValidNeighbours(graph, i, j, n, m);
        for (List<Integer> neighbour : neighbours) {
            Integer x = neighbour.getFirst(), y = neighbour.getLast();
            Solution.dfs(graph, x, y, n, m);
        }
    }

    public static Integer getCountOfEnclaves(List<List<Integer>> graph) {
        int n = graph.size(), m = graph.getFirst().size();

        for (int j = 0; j < m - 1; j += 1) {
            if (graph.getFirst().get(j).equals(1)) {
                Solution.dfs(graph, 0, j, n, m);
            }
        }

        for (int i = 0; i < n - 1; i += 1) {
            if (graph.get(i).getLast().equals(1)) {
                Solution.dfs(graph, i, m - 1, n, m);
            }
        }

        for (int j = m - 1; j > 0; j -= 1) {
            if (graph.getLast().get(j).equals(1)) {
                Solution.dfs(graph, n - 1, j, n, m);
            }
        }

        for (int i = n - 1; i > 0; i -= 1) {
            if (graph.get(i).getFirst().equals(1)) {
                Solution.dfs(graph, i, 0, n, m);
            }
        }

        Integer countOfEnclaves = 0;
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (graph.get(i).get(j).equals(1)) {
                    countOfEnclaves += 1;
                }
            }
        }

        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (graph.get(i).get(j).equals(2)) {
                    graph.get(i).set(j, 1);
                }
            }
        }

        return countOfEnclaves;
    }
}
