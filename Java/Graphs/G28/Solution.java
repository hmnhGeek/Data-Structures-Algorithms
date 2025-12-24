// Problem link - https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
// Solution - https://www.youtube.com/watch?v=C4gxoTaI71U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=28


package Graphs.G28;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


class Element<T> {
    public T node;
    public Integer distance;

    public Element(T node, Integer distance) {
        this.node = node;
        this.distance = distance;
    }
}


public class Solution {
    public static <T> Map<T, Integer> getShortestDistances(Map<T, List<T>> graph, T sourceNode) {
        /*
            Time complexity is O(V + E) and space complexity is O(V).
         */
        Map<T, Integer> distances = new HashMap<>();
        for (T node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
        }
        distances.put(sourceNode, 0);
        Queue<Element<T>> queue = new Queue<>();
        queue.push(new Element<>(sourceNode, 0));
        while (!queue.isEmpty()) {
            Element<T> element = queue.pop();
            for (T adjNode : graph.get(element.node)) {
                if (element.distance + 1 < distances.get(adjNode)) {
                    distances.put(adjNode, element.distance + 1);
                    queue.push(new Element<>(adjNode, distances.get(adjNode)));
                }
            }
        }
        return distances;
    }

    public static void main(String[] args) {
// Test 1: First graph, source 0
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(0, Arrays.asList(1, 3));
        graph1.put(1, Arrays.asList(0, 2));
        graph1.put(2, Arrays.asList(1, 6));
        graph1.put(3, Arrays.asList(0, 4));
        graph1.put(4, Arrays.asList(3, 5));
        graph1.put(5, Arrays.asList(4, 6));
        graph1.put(6, Arrays.asList(2, 5, 7, 8));
        graph1.put(7, Arrays.asList(6, 8));
        graph1.put(8, Arrays.asList(6, 7));
        System.out.println(Solution.getShortestDistances(graph1, 0));

        // Test 2: Second graph, source 3
        Map<Integer, List<Integer>> graph2 = new HashMap<>();
        graph2.put(0, Arrays.asList(3));
        graph2.put(1, Arrays.asList(3));
        graph2.put(2, Arrays.asList());
        graph2.put(3, Arrays.asList(0, 1));
        System.out.println(Solution.getShortestDistances(graph2, 3));

        // Test 3: Third graph, source 0
        Map<Integer, List<Integer>> graph3 = new HashMap<>();
        graph3.put(0, Arrays.asList(1, 3));
        graph3.put(1, Arrays.asList(0, 2));
        graph3.put(2, Arrays.asList(1));
        graph3.put(3, Arrays.asList(0, 4, 7));
        graph3.put(4, Arrays.asList(3, 5, 6, 7));
        graph3.put(5, Arrays.asList(4, 6));
        graph3.put(6, Arrays.asList(4, 5, 7));
        graph3.put(7, Arrays.asList(3, 4, 6));
        System.out.println(Solution.getShortestDistances(graph3, 0));
    }
}
