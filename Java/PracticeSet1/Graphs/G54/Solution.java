package PracticeSet1.Graphs.G54;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<List<T>> getStronglyConnectedComponents(Map<T, List<T>> graph) {
        Stack<T> stack = getSortedGraph(graph);
    }

    private static <T> Stack<T> getSortedGraph(Map<T, List<T>> graph) {
        Stack<T> stack = new Stack<>();
        Map<T, Boolean> visited = getVisitedArray(graph);
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                dfs(graph, node, stack, visited);
            }
        }
        return stack;
    }

    private static <T> void dfs(Map<T, List<T>> graph, T node, Stack<T> stack, Map<T, Boolean> visited) {
        visited.put(node, true);
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                dfs(graph, adjNode, stack, visited);
            }
        }
        stack.push(node);
    }

    private static <T> Map<T, Boolean> getVisitedArray(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        return visited;
    }
}
