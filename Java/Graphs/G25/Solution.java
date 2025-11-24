package Graphs.G25;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<T> getSafeNodes(Map<T, List<T>> graph) {
        Map<T, List<T>> reversedGraph = reverse(graph);
        Map<T, Integer> indegrees = getIndegrees(reversedGraph);
        Queue<T> queue = new Queue<>();
        for (T node : indegrees.keySet()) {
            if (indegrees.get(node) == 0) {
                queue.push(node);
            }
        }
        List<T> safeNodes = new ArrayList<>();
        while (!queue.isEmpty()) {
            T node = queue.pop();
            safeNodes.add(node);
            for (T adjNode : reversedGraph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) - 1);
                if (indegrees.get(adjNode) == 0) {
                    queue.push(adjNode);
                }
            }
        }
        return safeNodes;
    }

    private static <T> Map<T, Integer> getIndegrees(Map<T, List<T>> reversedGraph) {
        Map<T, Integer> indegrees = new HashMap<>();
        for (T node : reversedGraph.keySet()) {
            indegrees.put(node, 0);
        }
        for (T node : reversedGraph.keySet()) {
            for (T adjNode : reversedGraph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) + 1);
            }
        }
        return indegrees;
    }

    private static <T> Map<T, List<T>> reverse(Map<T, List<T>> graph) {
        Map<T, List<T>> reversed = new HashMap<>();
        for (T node : graph.keySet()) {
            reversed.put(node, new ArrayList<>());
        }
        for (T node : graph.keySet()) {
            for (T adjNode : graph.get(node)) {
                reversed.get(adjNode).add(node);
            }
        }
        return reversed;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.getSafeNodes(
                        Map.of(
                                0, List.of(1, 2),
                                1, List.of(3),
                                2, List.of(5),
                                3, List.of(0),
                                4, List.of(5),
                                5, List.of(),
                                6, List.of(),
                                7, List.of(1)
                        )
                )
        );

        System.out.println(
                Solution.getSafeNodes(
                        Map.of(
                                0, List.of(1),
                                1, List.of(2),
                                2, List.of(0, 3),
                                3, List.of()
                        )
                )
        );

        System.out.println(
                Solution.getSafeNodes(
                        Map.of(
                                0, List.of(1),
                                1, List.of(3),
                                2, List.of(4),
                                3, List.of(0, 2),
                                4, List.of()
                        )
                )
        );
    }
}
