// Problem link - https://www.geeksforgeeks.org/problems/eventual-safe-states/1
// Solution - https://www.youtube.com/watch?v=uRbJ1OF9aYM&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=20


package Graphs.G20;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        // Test Case 1
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(1, Arrays.asList(2));
        graph1.put(2, Arrays.asList(3));
        graph1.put(3, Arrays.asList(4, 5));
        graph1.put(4, Arrays.asList(6));
        graph1.put(5, Arrays.asList(6));
        graph1.put(6, Arrays.asList(7));
        graph1.put(7, Arrays.asList());
        graph1.put(8, Arrays.asList(1, 9));
        graph1.put(9, Arrays.asList(10));
        graph1.put(10, Arrays.asList(8));
        graph1.put(11, Arrays.asList(9));
        System.out.println(Solution.getSafeNodes(graph1));

        // Test Case 2
        Map<Integer, List<Integer>> graph2 = new HashMap<>();
        graph2.put(0, Arrays.asList(1, 2));
        graph2.put(1, Arrays.asList(2, 3));
        graph2.put(2, Arrays.asList(5));
        graph2.put(3, Arrays.asList(0));
        graph2.put(4, Arrays.asList(5));
        graph2.put(5, Arrays.asList());
        graph2.put(6, Arrays.asList());
        System.out.println(Solution.getSafeNodes(graph2));

        // Test Case 3
        Map<Integer, List<Integer>> graph3 = new HashMap<>();
        graph3.put(0, Arrays.asList(1));
        graph3.put(1, Arrays.asList(2));
        graph3.put(2, Arrays.asList(0, 3));
        graph3.put(3, Arrays.asList());
        System.out.println(Solution.getSafeNodes(graph3));

        // Test Case 4
        Map<Integer, List<Integer>> graph4 = new HashMap<>();
        graph4.put(0, Arrays.asList(1, 2, 3, 4));
        graph4.put(1, Arrays.asList(1, 2));
        graph4.put(2, Arrays.asList(3, 4));
        graph4.put(3, Arrays.asList(0, 4));
        graph4.put(4, Arrays.asList());
        System.out.println(Solution.getSafeNodes(graph4));
    }

    public static <T> Map<T, Boolean> getSafeNodes(Map<T, List<T>> graph) {
        /*
            Overall time complexity is O(V + E) and space is O(3V).
         */
        Map<T, Boolean> visited = getVisited(graph);
        Map<T, Boolean> pathVisited = getVisited(graph);
        Map<T, Boolean> safeNodes = getVisited(graph);
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                hasCycle(graph, node, visited, pathVisited, safeNodes);
            }
        }
        return safeNodes;
    }

    private static <T> boolean hasCycle(Map<T, List<T>> graph, T node, Map<T, Boolean> visited, Map<T, Boolean> pathVisited, Map<T, Boolean> safeNodes) {
        visited.put(node, true);
        pathVisited.put(node, true);

        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                if (hasCycle(graph, adjNode, visited, pathVisited, safeNodes)) {
                    return true;
                }
            } else if (pathVisited.get(adjNode)) {
                return true;
            }
        }

        pathVisited.put(node, false);
        // mark this node as safe as no adjacent node gave a cycle.
        safeNodes.put(node, true);
        return false;
    }

    private static <T> Map<T, Boolean> getVisited(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.putIfAbsent(node, false);
        }
        return visited;
    }
}
