package Graphs.G19;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static <T> Map<T, Boolean> getVisitedMap(Map<T, List<T>> graph) {
        Map<T, Boolean> map = new HashMap<>();
        for (T node : graph.keySet()) {
            map.putIfAbsent(node, false);
        }
        return map;
    }

    private static <T> boolean dfs(Map<T, List<T>> graph, T node, Map<T, Boolean> visited, Map<T, Boolean> pathVisited) {
        visited.put(node, true);
        pathVisited.put(node, true);
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                if (dfs(graph, adjNode, visited, pathVisited)) {
                    return true;
                }
            } else if (pathVisited.get(adjNode)) {
                return true;
            }
        }
        pathVisited.put(node, false);
        return false;
    }

    public static <T> boolean hasCycle(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = getVisitedMap(graph);
        Map<T, Boolean> pathVisited = getVisitedMap(graph);
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                if (dfs(graph, node, visited, pathVisited)) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.hasCycle(
                        Map.of(
                                1, List.of(2),
                                2, List.of(3),
                                3, List.of(4, 7),
                                4, List.of(5),
                                5, List.of(6),
                                6, List.of(),
                                7, List.of(5),
                                8, List.of(9),
                                9, List.of(10),
                                10, List.of(8)
                        )
                )
        );

        System.out.println(
                Solution.hasCycle(
                        Map.of(
                                0, List.of(1),
                                1, List.of(2),
                                2, List.of()
                        )
                )
        );

        System.out.println(
                Solution.hasCycle(
                        Map.of(
                                0, List.of(1, 2),
                                1, List.of(2),
                                2, List.of(0, 3),
                                3, List.of(3)
                        )
                )
        );

        System.out.println(
                Solution.hasCycle(
                        Map.of(
                                0, List.of(1, 2),
                                1, List.of(2),
                                2, List.of(3),
                                3, List.of()
                        )
                )
        );

        System.out.println(
                Solution.hasCycle(
                        Map.of(
                                0, List.of(1),
                                1, List.of(2, 5),
                                2, List.of(3),
                                3, List.of(4),
                                4, List.of(0, 1),
                                5, List.of()
                        )
                )
        );
    }
}
