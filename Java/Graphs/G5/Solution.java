package Graphs.G5;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<T> bfs(Map<T, List<T>> graph, T startNode) {
        if (!graph.containsKey(startNode)) return null;
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }

        Queue<T> queue = new Queue<>();
        queue.push(startNode);
        visited.put(startNode, true);
        List<T> result = new ArrayList<>();

        while (!queue.isEmpty()) {
            T node = queue.pop();
            result.add(node);
            for (T adjNode : graph.get(node)) {
                if (!visited.get(adjNode)) {
                    queue.push(adjNode);
                    visited.put(adjNode, true);
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(1, List.of(2, 6));
        graph1.put(2, List.of(1, 3, 4));
        graph1.put(3, List.of(2));
        graph1.put(4, List.of(2, 5));
        graph1.put(5, List.of(4, 7));
        graph1.put(6, List.of(1, 7, 8));
        graph1.put(7, List.of(5, 6));
        graph1.put(8, List.of(6));
        System.out.println(bfs(graph1, 1));
    }
}
