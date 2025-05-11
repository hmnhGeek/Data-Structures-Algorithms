package Graphs.G7;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static <T> void dfs(Map<T, List<T>> graph, T node, Map<T, Boolean> visited) {
        visited.put(node, true);
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                dfs(graph, adjNode, visited);
            }
        }
    }

    public static <T> Integer getNumberOfProvinces(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.putIfAbsent(node, false);
        }
        int numComponents = 0;
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                numComponents += 1;
                dfs(graph, node, visited);
            }
        }
        return numComponents;
    }

    public static void main(String[] args) {
        System.out.println(
            Solution.getNumberOfProvinces(
                Map.of(
                    0, Arrays.asList(2),
                    1, Arrays.asList(),
                    2, Arrays.asList(0)
                )
            )
        );

        System.out.println(
                Solution.getNumberOfProvinces(
                        Map.of(
                                0, Arrays.asList(1),
                                1, Arrays.asList(0)
                        )
                )
        );

        System.out.println(
                Solution.getNumberOfProvinces(
                        Map.of(
                                0, Arrays.asList(),
                                1, Arrays.asList(),
                                2, Arrays.asList()
                        )
                )
        );
    }
}
