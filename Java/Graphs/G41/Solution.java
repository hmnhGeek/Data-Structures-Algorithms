package Graphs.G41;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class Solution {
    public static <T> Map<T, Integer> getShortestPaths(Map<T, List<AdjacentNode<T>>> graph, T source) {
        if (!graph.containsKey(source)) return null;
        int n = graph.size();

        // make the distances map.
        Map<T, Integer> distances = new HashMap<>();
        for (T node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
        }
        distances.put(source, 0);

        List<Edge<T>> edgeRepresentation = getEdgeRepresentation(graph);
        for (int i = 0; i < n - 1; i += 1) {
            for (Edge<T> currentEdge : edgeRepresentation) {
                if (distances.get(currentEdge.source) != Integer.MAX_VALUE &&
                        distances.get(currentEdge.source) + currentEdge.edgeWeight < distances.get(currentEdge.destination)) {
                    distances.put(currentEdge.destination, distances.get(currentEdge.source) + currentEdge.edgeWeight);
                }
            }
        }

        // negative cycle if on n-th iteration the weights change.
        for (Edge<T> currentEdge : edgeRepresentation) {
            if (distances.get(currentEdge.source) != Integer.MAX_VALUE &&
                    distances.get(currentEdge.source) + currentEdge.edgeWeight < distances.get(currentEdge.destination)) {
                return null;
            }
        }
        return distances;
    }

    private static <T> List<Edge<T>> getEdgeRepresentation(Map<T, List<AdjacentNode<T>>> graph) {
        List<Edge<T>> edges = new ArrayList<>();
        for (T node : graph.keySet()) {
            for (AdjacentNode<T> adjacentNode : graph.get(node)) {
                edges.add(new Edge<>(node, adjacentNode.node, adjacentNode.edgeWeight));
            }
        }
        return edges;
    }

    public static void main(String[] args) {
        // Test case 1: Simple graph with one edge
        Map<Integer, List<AdjacentNode<Integer>>> graph1 = new HashMap<>();
        graph1.put(0, List.of(new AdjacentNode<>(1, 9)));
        graph1.put(1, new ArrayList<>());
        System.out.println("Test 1: " + getShortestPaths(graph1, 0));

        // Test case 2: Graph with negative edge but no negative cycle
        Map<Integer, List<AdjacentNode<Integer>>> graph2 = new HashMap<>();
        graph2.put(0, List.of(new AdjacentNode<>(1, 5)));
        graph2.put(1, List.of(new AdjacentNode<>(0, 3), new AdjacentNode<>(2, -1)));
        graph2.put(2, List.of(new AdjacentNode<>(0, 1)));
        System.out.println("Test 2: " + getShortestPaths(graph2, 2));

        // Test case 3: Graph with negative edge but no negative cycle
        Map<Integer, List<AdjacentNode<Integer>>> graph3 = new HashMap<>();
        graph3.put(0, List.of(new AdjacentNode<>(1, 5)));
        graph3.put(1, List.of(new AdjacentNode<>(2, 1), new AdjacentNode<>(3, 2)));
        graph3.put(2, List.of(new AdjacentNode<>(4, 1)));
        graph3.put(3, new ArrayList<>());
        graph3.put(4, List.of(new AdjacentNode<>(3, -1)));
        System.out.println("Test 3: " + getShortestPaths(graph3, 0));

        // Test case 4: Graph with negative cycle
        Map<Integer, List<AdjacentNode<Integer>>> graph4 = new HashMap<>();
        graph4.put(0, List.of(new AdjacentNode<>(1, 4)));
        graph4.put(1, List.of(new AdjacentNode<>(2, -6)));
        graph4.put(2, List.of(new AdjacentNode<>(3, 5)));
        graph4.put(3, List.of(new AdjacentNode<>(1, -2)));
        System.out.println("Test 4: " + getShortestPaths(graph4, 0));

        // Test case 5: Larger graph with negative edges but no negative cycle
        Map<Integer, List<AdjacentNode<Integer>>> graph5 = new HashMap<>();
        graph5.put(0, List.of(new AdjacentNode<>(1, 5)));
        graph5.put(1, List.of(new AdjacentNode<>(2, -2), new AdjacentNode<>(5, -3)));
        graph5.put(2, List.of(new AdjacentNode<>(4, 3)));
        graph5.put(3, List.of(new AdjacentNode<>(2, 6), new AdjacentNode<>(4, -2)));
        graph5.put(4, new ArrayList<>());
        graph5.put(5, List.of(new AdjacentNode<>(3, 1)));
        System.out.println("Test 5: " + getShortestPaths(graph5, 0));
    }
}
