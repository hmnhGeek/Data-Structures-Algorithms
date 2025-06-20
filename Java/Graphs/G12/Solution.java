package Graphs.G12;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static <T> Map<T, Boolean> getVisited(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        return visited;
    }

    public static <T> Boolean hasCycle(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = getVisited(graph);
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                if (dfs(graph, node, null, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    private static <T> boolean dfs(Map<T, List<T>> graph, T node, T parent, Map<T, Boolean> visited) {
        visited.put(node, true);
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                if (dfs(graph, adjNode, node, visited)) {
                    return true;
                }
            } else if (adjNode != parent) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph1 = Map.of(
                1, List.of(2, 3),
                2, List.of(1, 5),
                3, List.of(1, 4, 6),
                4, List.of(3),
                5, List.of(2, 7),
                6, List.of(3, 7),
                7, List.of(5, 6)
        );
        System.out.println(Solution.hasCycle(graph1));

        Map<Integer, List<Integer>> graph2 = Map.of(
                1, List.of(2, 3),
                2, List.of(1, 5),
                3, List.of(1, 4, 6),
                4, List.of(3),
                5, List.of(2, 7),
                6, List.of(3),
                7, List.of(5)
        );
        System.out.println(Solution.hasCycle(graph2));

        Map<Integer, List<Integer>> graph3 = Map.of(
                0, List.of(1, 2),
                1, List.of(0, 2),
                2, List.of(0, 1, 3),
                3, List.of(2)
        );
        System.out.println(Solution.hasCycle(graph3));

        Map<Integer, List<Integer>> graph4 = Map.of(
                0, List.of(1),
                1, List.of(0, 2),
                2, List.of(1, 3),
                3, List.of(2)
        );
        System.out.println(Solution.hasCycle(graph4));

        Map<Integer, List<Integer>> graph5 = Map.of(
                0, List.of(),
                1, List.of(2),
                2, List.of(1, 3),
                3, List.of(2)
        );
        System.out.println(Solution.hasCycle(graph5));

        Map<Integer, List<Integer>> graph6 = Map.of(
                0, List.of(1),
                1, List.of(0, 2, 4),
                2, List.of(1, 3),
                3, List.of(2, 4),
                4, List.of(1, 3)
        );
        System.out.println(Solution.hasCycle(graph6));
    }

}
