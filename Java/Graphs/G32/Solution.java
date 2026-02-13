package Graphs.G32;

import Graphs.G32.MinHeap.Heap;
import Graphs.G32.MinHeap.MinHeap;

import java.util.*;


class HeapElement<T extends Comparable<T>> implements Comparable<HeapElement<T>> {
    public Integer weight;
    public T node;

    public HeapElement(Integer weight, T node) {
        this.weight = weight;
        this.node = node;
    }

    @Override
    public int compareTo(HeapElement<T> o2) {
        if (weight > o2.weight) return 1;
        if (weight.equals(o2.weight)) {
            if (node.compareTo(o2.node) > 0) {
                return 1;
            } else if (node.compareTo(o2.node) < 0) {
                return -1;
            } else {
                return 0;
            }
        } else {
            return -1;
        }
    }

    @Override
    public String toString() {
        return String.format("(%d, %s)", weight, node);
    }
}


class Edge<T> {
    public T node;
    public Integer weight;

    public Edge(T node, Integer weight) {
        this.node = node;
        this.weight = weight;
    }
}


public class Solution {
    public static void main(String[] args) {
        // Example 1
        Map<Integer, List<Edge<Integer>>> graph1 = new HashMap<>();

        graph1.put(0, Arrays.asList(new Edge<>(1, 4), new Edge<>(2, 4)));
        graph1.put(1, Arrays.asList(new Edge<>(0, 4), new Edge<>(2, 2)));
        graph1.put(2, Arrays.asList(
                new Edge<>(0, 4),
                new Edge<>(1, 2),
                new Edge<>(3, 3),
                new Edge<>(5, 6),
                new Edge<>(4, 1)
        ));
        graph1.put(3, Arrays.asList(new Edge<>(2, 3), new Edge<>(5, 2)));
        graph1.put(4, Arrays.asList(new Edge<>(2, 1), new Edge<>(5, 3)));
        graph1.put(5, Arrays.asList(
                new Edge<>(3, 2),
                new Edge<>(2, 6),
                new Edge<>(4, 3)
        ));

        System.out.println(getMinDistances(graph1, 0));

        // Example 2
        Map<Integer, List<Edge<Integer>>> graph2 = new HashMap<>();

        graph2.put(0, Arrays.asList(new Edge<>(1, 9)));
        graph2.put(1, Arrays.asList(new Edge<>(0, 9)));

        System.out.println(getMinDistances(graph2, 0));

        // Example 3
        Map<Integer, List<Edge<Integer>>> graph3 = new HashMap<>();

        graph3.put(0, Arrays.asList(new Edge<>(1, 1), new Edge<>(2, 6)));
        graph3.put(1, Arrays.asList(new Edge<>(0, 1), new Edge<>(2, 3)));
        graph3.put(2, Arrays.asList(new Edge<>(0, 6), new Edge<>(1, 3)));

        System.out.println(getMinDistances(graph3, 2));

    }

    public static <T extends Comparable<T>> Map<T, Integer> getMinDistances(Map<T, List<Edge<T>>> graph, T sourceNode) {
        if (!graph.containsKey(sourceNode)) return null;
        MinHeap<HeapElement<T>> minHeap = new MinHeap<>();
        minHeap.insert(new HeapElement<>(0, sourceNode));
        Map<T, Integer> distances = new HashMap<>();
        for (T node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
        }
        distances.put(sourceNode, 0);
        while (!minHeap.isEmpty()) {
            HeapElement<T> heapElement = minHeap.pop();
            for (Edge<T> edge : graph.get(heapElement.node)) {
                T adjNode = edge.node;
                Integer weight = edge.weight;
                if (heapElement.weight + weight < distances.get(adjNode)) {
                    Integer newWeight = heapElement.weight + weight;
                    distances.put(adjNode, newWeight);
                    minHeap.insert(new HeapElement<>(newWeight, adjNode));
                }
            }
        }
        return distances;
    }
}
