// Problem link - https://www.geeksforgeeks.org/strongly-connected-components/
// Solution - https://www.youtube.com/watch?v=R6uoSjZ2imo&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=54


package PracticeSet1.Graphs.G54;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<List<T>> getStronglyConnectedComponents(Map<T, List<T>> graph) {
        /*
            Overall time complexity is O(V + E) and space complexity is O(V + E).
         */
        Stack<T> stack = getSortedGraph(graph);
        Map<T, List<T>> reversedGraph = reverseGraph(graph);
        List<List<T>> scc = getSCCs(reversedGraph, stack);
        return scc;
    }

    private static <T> List<List<T>> getSCCs(Map<T, List<T>> reversedGraph, Stack<T> stack) {
        List<List<T>> scc = new ArrayList<>();
        Map<T, Boolean> visited = getVisitedArray(reversedGraph);
        while (!stack.isEmpty()) {
            T node = stack.pop();
            if (!visited.get(node)) {
                List<T> component = new ArrayList<>();
                dfs(reversedGraph, node, component, visited);
                scc.add(component);
            }
        }
        return scc;
    }

    private static <T> void dfs(Map<T, List<T>> reversedGraph, T node, List<T> component, Map<T, Boolean> visited) {
        visited.put(node, true);
        component.add(node);
        for (T adjNode : reversedGraph.get(node)) {
            if (!visited.get(adjNode)) {
                dfs(reversedGraph, adjNode, component, visited);
            }
        }
    }

    private static <T> Map<T, List<T>> reverseGraph(Map<T, List<T>> graph) {
        Map<T, List<T>> reversedGraph = new HashMap<>();
        for (T node : graph.keySet()) reversedGraph.put(node, new ArrayList<>());
        for (T node : graph.keySet()) {
            for (T adjNode : graph.get(node)) {
                reversedGraph.get(adjNode).add(node);
            }
        }
        return reversedGraph;
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

    public static void main(String[] args) {
        System.out.println(getStronglyConnectedComponents(
                Map.of(
                        0, List.of(1),
                        1, List.of(2),
                        2, List.of(0, 3),
                        3, List.of(4),
                        4, List.of(5, 7),
                        5, List.of(6),
                        6, List.of(4, 7),
                        7, List.of()
                )
        ));

        System.out.println(getStronglyConnectedComponents(
                Map.of(
                        0, List.of(2, 3),
                        1, List.of(0),
                        2, List.of(1),
                        3, List.of(4),
                        4, List.of()
                )
        ));

        System.out.println(getStronglyConnectedComponents(
                Map.of(
                        0, List.of(1),
                        1, List.of(2),
                        2, List.of(0)
                )
        ));

        System.out.println(getStronglyConnectedComponents(
                Map.of(
                        1, List.of(2),
                        2, List.of(3, 4),
                        3, List.of(4, 6),
                        4, List.of(1, 5),
                        5, List.of(6),
                        6, List.of(7),
                        7, List.of(5)
                )
        ));
    }
}
