package Graphs.G27;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Utility {
    public static <T> Stack<T> getTopologicalSort(Map<T, List<GraphElement<T>>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        Stack<T> stack = new Stack<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                dfs(graph, node, stack, visited);
            }
        }
        return stack;
    }

    private static <T> void dfs(Map<T, List<GraphElement<T>>> graph, T node, Stack<T> stack, Map<T, Boolean> visited) {
        visited.put(node, true);
        for (GraphElement<T> graphElement : graph.get(node)) {
            T adjNode = graphElement.adjNode;
            if (!visited.get(adjNode)) {
                dfs(graph, adjNode, stack, visited);
            }
        }
        stack.push(node);
    }
}
