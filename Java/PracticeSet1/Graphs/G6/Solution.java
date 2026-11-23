package PracticeSet1.Graphs.G6;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
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
        System.out.println(Graphs.G6.Solution.dfs(graph1));

        Map<Integer, List<Integer>> graph2 = new HashMap<>();
        graph2.put(0, List.of(1, 2, 3));
        graph2.put(1, List.of(0));
        graph2.put(2, List.of(0, 4));
        graph2.put(3, List.of(0));
        graph2.put(4, List.of(2));
        System.out.println(Graphs.G6.Solution.dfs(graph2));

        Map<Integer, List<Integer>> graph3 = new HashMap<>();
        graph3.put(0, List.of(1, 2));
        graph3.put(1, List.of(0, 2));
        graph3.put(2, List.of(1, 0, 3, 4));
        graph3.put(3, List.of(2));
        graph3.put(4, List.of(2));
        System.out.println(Graphs.G6.Solution.dfs(graph3));

        Map<Integer, List<Integer>> graph4 = new HashMap<>();
        graph4.put(0, List.of(1));
        graph4.put(1, List.of(0, 2));
        graph4.put(2, List.of(1));
        graph4.put(3, List.of(4));
        graph4.put(4, List.of(3));
        System.out.println(Graphs.G6.Solution.dfs(graph4));
    }

    public static <T> List<T> getDFS(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = getBlankVisitedMap(graph);
        List<T> traversal = new ArrayList<>();
        for (T node : graph.keySet()) {
            // if the node is not visited, initiate a DFS from it in O(V + E) time.
            if (!visited.get(node)) {
                getDFS(graph, node, visited, traversal);
            }
        }
        return traversal;
    }

    private static <T> void getDFS(Map<T, List<T>> graph, T node, Map<T, Boolean> visited, List<T> traversal) {
        visited.put(node, true);
        traversal.add(node);
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                getDFS(graph, adjNode, visited, traversal);
            }
        }
    }

    private static <T> Map<T, Boolean> getBlankVisitedMap(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        return visited;
    }
}
