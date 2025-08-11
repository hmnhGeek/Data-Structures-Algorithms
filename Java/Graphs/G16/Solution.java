// Problem link - https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1
// Solution - https://www.youtube.com/watch?v=7zmgQSJghpo&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=17


package Graphs.G16;

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                getDistinctIslandsCount(
                        Arrays.asList(
                                Arrays.asList(1, 1, 0, 0, 0),
                                Arrays.asList(1, 1, 0, 0, 0),
                                Arrays.asList(0, 0, 0, 1, 1),
                                Arrays.asList(0, 0, 0, 1, 1)
                        )
                )
        );

        System.out.println(
                getDistinctIslandsCount(
                        Arrays.asList(
                                Arrays.asList(1, 1, 0, 1, 1),
                                Arrays.asList(1, 0, 0, 0, 0),
                                Arrays.asList(0, 0, 0, 0, 1),
                                Arrays.asList(1, 1, 0, 1, 1)
                        )
                )
        );

        System.out.println(
                getDistinctIslandsCount(
                        Arrays.asList(
                                Arrays.asList(1, 1, 0),
                                Arrays.asList(0, 0, 1),
                                Arrays.asList(0, 0, 1)
                        )
                )
        );
    }

    public static Integer getDistinctIslandsCount(List<List<Integer>> graph) {
        /*
            Time complexity is O(nm) and space complexity is O(nm).
         */
        int n = graph.size(), m = graph.getFirst().size();
        List<List<Boolean>> visited = getBlankVisitedArray(graph, n, m);
        Set<List<List<Integer>>> distinctIslands = new HashSet<>();
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (graph.get(i).get(j) == 1 && !visited.get(i).get(j)) {
                    List<List<Integer>> island = new ArrayList<>();
                    dfs(graph, i, j, visited, i, j, island, n, m);
                    distinctIslands.add(island);
                }
            }
        }
        return distinctIslands.size();
    }

    private static void dfs(List<List<Integer>> graph, int i, int j, List<List<Boolean>> visited, int baseX, int baseY, List<List<Integer>> island, int n, int m) {
        visited.get(i).set(j, true);
        island.add(List.of(baseX - i, baseY - j));
        // following RDLU order
        if (0 <= j + 1 && j + 1 < m && graph.get(i).get(j + 1).equals(1) && !visited.get(i).get(j + 1)) {
            dfs(graph, i, j + 1, visited, baseX, baseY, island, n, m);
        }
        if (0 <= i + 1 && i + 1 < n && graph.get(i + 1).get(j).equals(1) && !visited.get(i + 1).get(j)) {
            dfs(graph, i + 1, j, visited, baseX, baseY, island, n, m);
        }
        if (0 <= j - 1 && j - 1 < m && graph.get(i).get(j - 1).equals(1) && !visited.get(i).get(j - 1)) {
            dfs(graph, i, j - 1, visited, baseX, baseY, island, n, m);
        }
        if (0 <= i - 1 && i - 1 < n && graph.get(i - 1).get(j).equals(1) && !visited.get(i - 1).get(j)) {
            dfs(graph, i - 1, j, visited, baseX, baseY, island, n, m);
        }
    }

    private static List<List<Boolean>> getBlankVisitedArray(List<List<Integer>> graph, int n, int m) {
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
