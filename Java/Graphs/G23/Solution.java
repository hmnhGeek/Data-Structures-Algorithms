package Graphs.G23;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> boolean detectCycle(Map<T, List<T>> graph) {
        Map<T, Integer> indegrees = getIndegrees(graph);
        Queue<T> queue = new Queue<>();
        for (T node : indegrees.keySet()) {
            if (indegrees.get(node) == 0) {
                queue.push(node);
            }
        }
        int count = 0;
        while (!queue.isEmpty()) {
            T node = queue.pop();
            count += 1;
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) - 1);
                if (indegrees.get(adjNode) == 0) {
                    queue.push(adjNode);
                }
            }
        }
        return count != graph.size();
    }

    private static <T> Map<T, Integer> getIndegrees(Map<T, List<T>> graph) {
        Map<T, Integer> indegrees = new HashMap<>();
        for (T node : graph.keySet()) {
            indegrees.put(node, 0);
        }
        for (T node : graph.keySet()) {
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.getOrDefault(adjNode, 0) + 1);
            }
        }
        return indegrees;
    }

    public static void main(String[] args) {
        System.out.println(
                detectCycle(Map.of(
                        0, List.of(1),
                        1, List.of(2),
                        2, List.of(3),
                        3, List.of(3)
                ))
        );

        System.out.println(
                detectCycle(Map.of(
                        0, List.of(1),
                        1, List.of(2),
                        2, List.of()
                ))
        );

        System.out.println(
                detectCycle(Map.of(
                        0, List.of(1, 2),
                        1, List.of(2),
                        2, List.of(0, 3),
                        3, List.of(3)
                ))
        );

        System.out.println(
                detectCycle(Map.of(
                        0, List.of(1, 2),
                        1, List.of(2),
                        2, List.of(3),
                        3, List.of()
                ))
        );
    }
}
