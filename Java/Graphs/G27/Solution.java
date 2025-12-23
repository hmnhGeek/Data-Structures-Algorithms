// Problem link - https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
// Solution - https://www.youtube.com/watch?v=ZUFQfFaU-8U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=27


package Graphs.G27;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> Map<T, Integer> getShortestPaths(Map<T, List<GraphElement<T>>> graph) {
        Stack<T> topologicalSort = Utility.getTopologicalSort(graph);
        Map<T, Integer> distances = new HashMap<>();
        for (T node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
        }
        distances.put(topologicalSort.top(), 0);
        System.out.println(String.format("Source node is %s", topologicalSort.top()));
        while (!topologicalSort.isEmpty()) {
            T node = topologicalSort.pop();
            for (GraphElement<T> graphElement : graph.get(node)) {
                T adjNode = graphElement.adjNode;
                if (distances.get(node) + graphElement.weight < distances.get(adjNode)) {
                    distances.put(adjNode, distances.get(node) + graphElement.weight);
                }
            }
        }
        return distances;
    }

    public static void main(String[] args) {
        Map<Integer, List<GraphElement<Integer>>> graph1 = new HashMap<>();
        graph1.put(0, Arrays.asList(new GraphElement<>(1, 2)));
        graph1.put(1, Arrays.asList(new GraphElement<>(3, 1)));
        graph1.put(2, Arrays.asList(new GraphElement<>(3, 3)));
        graph1.put(3, Arrays.asList());
        graph1.put(4, Arrays.asList(new GraphElement<>(0, 3), new GraphElement<>(2, 1)));
        graph1.put(5, Arrays.asList(new GraphElement<>(4, 1)));
        graph1.put(6, Arrays.asList(new GraphElement<>(4, 2), new GraphElement<>(5, 3)));
        System.out.println(getShortestPaths(graph1));

        // Test case 2
        Map<Integer, List<GraphElement<Integer>>> graph2 = new HashMap<>();
        graph2.put(0, Arrays.asList(new GraphElement<>(1, 2), new GraphElement<>(2, 1)));
        graph2.put(1, Arrays.asList());
        graph2.put(2, Arrays.asList());
        System.out.println(getShortestPaths(graph2));

        // Test case 3
        Map<Integer, List<GraphElement<Integer>>> graph3 = new HashMap<>();
        graph3.put(0, Arrays.asList(new GraphElement<>(2, 4)));
        graph3.put(1, Arrays.asList(new GraphElement<>(0, 3), new GraphElement<>(2, 2), new GraphElement<>(3, 5)));
        graph3.put(2, Arrays.asList(new GraphElement<>(4, 2), new GraphElement<>(3, -3)));
        graph3.put(3, Arrays.asList());
        graph3.put(4, Arrays.asList(new GraphElement<>(3, 2)));
        System.out.println(getShortestPaths(graph3));
    }
}
