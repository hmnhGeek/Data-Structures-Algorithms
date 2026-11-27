package PracticeSet1.Graphs.G7;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                Graphs.G7.Solution.getNumberOfProvinces(
                        Map.of(
                                0, Arrays.asList(2),
                                1, Arrays.asList(),
                                2, Arrays.asList(0)
                        )
                )
        );

        System.out.println(
                Graphs.G7.Solution.getNumberOfProvinces(
                        Map.of(
                                0, Arrays.asList(1),
                                1, Arrays.asList(0)
                        )
                )
        );

        System.out.println(
                Graphs.G7.Solution.getNumberOfProvinces(
                        Map.of(
                                0, Arrays.asList(),
                                1, Arrays.asList(),
                                2, Arrays.asList()
                        )
                )
        );
    }

    public static <T> Integer getNumProvinces(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = initVisitedMap(graph);
        int numProvinces = 0;
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                numProvinces += 1;
                dfs(node, graph, visited);
            }
        }
        return numProvinces;
    }

    private static <T> void dfs(T node, Map<T, List<T>> graph, Map<T, Boolean> visited) {
        visited.put(node, true);
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                dfs(adjNode, graph, visited);
            }
        }
    }

    private static <T> Map<T, Boolean> initVisitedMap(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        return visited;
    }
}
