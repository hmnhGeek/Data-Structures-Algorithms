package Graphs.G21;

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(0, Arrays.asList());
        graph1.put(1, Arrays.asList());
        graph1.put(2, Arrays.asList(3));
        graph1.put(3, Arrays.asList(1));
        graph1.put(4, Arrays.asList(0, 1));
        graph1.put(5, Arrays.asList(0, 2));
        System.out.println(getTopologicalSort(graph1));

        Map<Integer, List<Integer>> graph2 = new HashMap<>();
        graph2.put(0, Arrays.asList());
        graph2.put(1, Arrays.asList(0));
        graph2.put(2, Arrays.asList(0));
        graph2.put(3, Arrays.asList(0));
        System.out.println(getTopologicalSort(graph2));

        Map<Integer, List<Integer>> graph3 = new HashMap<>();
        graph3.put(0, Arrays.asList());
        graph3.put(1, Arrays.asList(3));
        graph3.put(2, Arrays.asList(3));
        graph3.put(3, Arrays.asList());
        graph3.put(4, Arrays.asList(0, 1));
        graph3.put(5, Arrays.asList(0, 2));
        System.out.println(getTopologicalSort(graph3));
    }

    public static <T> List<T> getTopologicalSort(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = getVisitedMap(graph);
        Stack<T> stack = new Stack<>();
        List<T> result = new ArrayList<>();
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                dfs(graph, node, stack, visited);
            }
        }
        while (!stack.isEmpty()) {
            result.add(stack.pop());
        }
        return result;
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

    private static <T> Map<T, Boolean> getVisitedMap(Map<T, List<T>> graph) {
        Map<T, Boolean> map = new HashMap<>();
        for (T node : graph.keySet()) {
            map.put(node, false);
        }
        return map;
    }

}
