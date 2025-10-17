// Problem link - https://www.geeksforgeeks.org/problems/topological-sort/1
// Solution - https://www.youtube.com/watch?v=73sneFXuTEg&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=22


package Graphs.G22;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<T> topologicalSort(Map<T, List<T>> graph) {
        /*
            Time complexity is O(V + E) and space complexity is O(V).
         */

        Map<T, Integer> indegrees = new HashMap<>();
        for (T node : graph.keySet()) {
            indegrees.putIfAbsent(node, 0);
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.getOrDefault(adjNode, 0) + 1);
            }
        }

        Queue<T> queue = new Graphs.G22.Queue<>();
        for (T node : indegrees.keySet()) {
            if (indegrees.get(node) == 0) {
                queue.push(node);
            }
        }

        List<T> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            T node = queue.pop();
            result.add(node);
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) - 1);
                if (indegrees.get(adjNode) == 0) {
                    queue.push(adjNode);
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(0, List.of());
        graph1.put(1, List.of());
        graph1.put(2, List.of(3));
        graph1.put(3, List.of(1));
        graph1.put(4, List.of(0, 1));
        graph1.put(5, List.of(0, 2));

        Map<Integer, List<Integer>> graph2 = new HashMap<>();
        graph2.put(0, List.of());
        graph2.put(1, List.of(0));
        graph2.put(2, List.of(0));
        graph2.put(3, List.of(0));

        Map<Integer, List<Integer>> graph3 = new HashMap<>();
        graph3.put(0, List.of());
        graph3.put(1, List.of(3));
        graph3.put(2, List.of(3));
        graph3.put(3, List.of());
        graph3.put(4, List.of(0, 1));
        graph3.put(5, List.of(0, 2));

        System.out.println("Topological Sort of graph1: " + topologicalSort(graph1));
        System.out.println("Topological Sort of graph2: " + topologicalSort(graph2));
        System.out.println("Topological Sort of graph3: " + topologicalSort(graph3));
    }
}
