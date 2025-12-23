package Graphs.G27;

import java.lang.reflect.Array;
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
    }
}
