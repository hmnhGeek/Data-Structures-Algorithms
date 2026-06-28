// Problem link - https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
// Solution - https://www.youtube.com/watch?v=mJcZjjKzeqk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=45


package Graphs.G45;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


class Edge<T> {
    public T adjNode;
    public Integer edgeWt;

    public Edge(T adjNode, Integer edgeWt) {
        this.adjNode = adjNode;
        this.edgeWt = edgeWt;
    }
}


public class Solution {
    public static <T> List<List<T>> getMST(Map<T, List<Edge<T>>> graph, T sourceNode) {
        /*
            Time complexity is O(E log(E)) and space complexity is O(V + E).
         */
        MinHeap<HeapElement<T>> pq = new MinHeap<>();
        List<List<T>> mst = new ArrayList<>();
        pq.insert(new HeapElement<>(0, sourceNode, null));
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        while (!pq.isEmpty()) {
            HeapElement<T> heapElement = pq.pop();
            Integer wt = heapElement.weight;
            T node = heapElement.node, parent = heapElement.parent;
            if (visited.get(node).equals(Boolean.TRUE)) {
                continue;
            }
            visited.put(node, true);
            if (parent != null) {
                mst.add(List.of(node, parent));
            }
            for (Edge<T> edge : graph.get(node)) {
                T adjNode = edge.adjNode;
                Integer edgeWt = edge.edgeWt;
                pq.insert(new HeapElement<>(edgeWt, adjNode, node));
            }
        }
        return mst;
    }

    public static void main(String[] args) {
        Map<Integer, List<Edge<Integer>>> graph1 = new HashMap<>();
        graph1.put(0, List.of(new Edge<>(1, 2), new Edge<>(2, 1)));
        graph1.put(1, List.of(new Edge<>(0, 2), new Edge<>(2, 1)));
        graph1.put(2, List.of(new Edge<>(0, 1), new Edge<>(1, 1), new Edge<>(4, 2), new Edge<>(3, 2)));
        graph1.put(3, List.of(new Edge<>(2, 2), new Edge<>(4, 1)));
        graph1.put(4, List.of(new Edge<>(2, 2), new Edge<>(3, 1)));

        System.out.println(Solution.getMST(graph1, 0));

        Map<Integer, List<Edge<Integer>>> graph2 = new HashMap<>();
        graph2.put(0, List.of(new Edge<>(1, 5), new Edge<>(2, 1)));
        graph2.put(1, List.of(new Edge<>(0, 5), new Edge<>(2, 3)));
        graph2.put(2, List.of(new Edge<>(0, 1), new Edge<>(1, 3)));

        System.out.println(Solution.getMST(graph2, 0));

        Map<Integer, List<Edge<Integer>>> graph3 = new HashMap<>();
        graph3.put(0, List.of(new Edge<>(1, 1), new Edge<>(2, 3), new Edge<>(3, 4)));
        graph3.put(1, List.of(new Edge<>(0, 1), new Edge<>(2, 2)));
        graph3.put(2, List.of(new Edge<>(1, 2), new Edge<>(0, 3), new Edge<>(3, 5)));
        graph3.put(3, List.of(new Edge<>(0, 4), new Edge<>(2, 5)));

        System.out.println(Solution.getMST(graph3, 0));
    }
}
