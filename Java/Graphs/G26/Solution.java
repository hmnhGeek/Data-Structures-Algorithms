package Graphs.G26;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static <T> List<T> getTopologicalSort(Map<T, List<T>> graph) {
        Map<T, Integer> indegrees = getIndegrees(graph);
        Queue<T> queue = new Queue<>();
        List<T> result = new ArrayList<>();
        for (T node : indegrees.keySet()) {
            if (indegrees.get(node).equals(0)) {
                queue.push(node);
            }
        }
        while (!queue.isEmpty()) {
            T node = queue.pop();
            result.add(node);
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) - 1);
                if (indegrees.get(adjNode).equals(0)) {
                    queue.push(adjNode);
                }
            }
        }
        return result;
    }

    private static <T> Map<T, Integer> getIndegrees(Map<T, List<T>> graph) {
        Map<T, Integer> indegrees = new HashMap<>();
        for (T node : graph.keySet()) {
            indegrees.put(node, 0);
        }
        for (T node : graph.keySet()) {
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) + 1);
            }
        }
        return indegrees;
    }
}
