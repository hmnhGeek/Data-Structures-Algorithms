package Graphs.G6;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static <T> void dfs(Map<T, List<T>> graph, T node, Map<T, Boolean> visited, List<T> result) {
        visited.put(node, true);
        result.add(node);
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                dfs(graph, adjNode, visited, result);
            }
        }
    }

    public static <T> List<T> dfs(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }

        List<T> result = new ArrayList<>();

        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                dfs(graph, node, visited, result);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(1, List.of(2, 3));
        graph1.put(2, List.of(1, 5, 6));
        graph1.put(3, List.of(1, 4, 7));
        graph1.put(4, List.of(3, 8));
        graph1.put(5, List.of(2));
        graph1.put(6, List.of(2));
        graph1.put(7, List.of(3, 8));
        graph1.put(8, List.of(4, 7));
        System.out.println(Solution.dfs(graph1));
    }
}
