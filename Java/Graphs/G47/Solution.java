// Problem link - https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
// Solution - https://www.youtube.com/watch?v=DMnDM_sxVig&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=47


package Graphs.G47;


import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                getMST(
                        Map.of(
                                1, List.of(
                                        new Edge<>(2, 1, 2),
                                        new Edge<>(1, 1, 4),
                                        new Edge<>(4, 1, 5)
                                ),
                                2, List.of(
                                        new Edge<>(2, 2, 1),
                                        new Edge<>(3, 2, 3),
                                        new Edge<>(3, 2, 4),
                                        new Edge<>(7, 2, 6)
                                ),
                                3, List.of(
                                        new Edge<>(3, 3, 2),
                                        new Edge<>(5, 3, 4),
                                        new Edge<>(8, 3, 6)
                                ),
                                4, List.of(
                                        new Edge<>(9, 4, 5),
                                        new Edge<>(1, 4, 1),
                                        new Edge<>(3, 4, 2),
                                        new Edge<>(5, 4, 3)
                                ),
                                5, List.of(
                                        new Edge<>(4, 5, 1),
                                        new Edge<>(9, 5, 4)
                                ),
                                6, List.of(
                                        new Edge<>(7, 6, 2),
                                        new Edge<>(8, 6, 3)
                                )
                        )
                )
        );

        System.out.println(
                getMST(
                        Map.of(
                                0, List.of(
                                        new Edge<>(5, 0, 1),
                                        new Edge<>(1, 0, 2)
                                ),
                                1, List.of(
                                        new Edge<>(5, 1, 0),
                                        new Edge<>(3, 1, 2)
                                ),
                                2, List.of(
                                        new Edge<>(1, 2, 0),
                                        new Edge<>(3, 2, 1)
                                )
                        )
                )
        );
    }

    public static <T> List<Edge<T>> getMST(Map<T, List<Edge<T>>> graph) {
        List<Edge<T>> mst = new ArrayList<>();
        List<Edge<T>> edges = getEdges(graph);
        QuickSort.sort(edges);
        DisjointSet<T> ds = new DisjointSet<>(graph.keySet().stream().toList());
        for (Edge<T> edge : edges) {
            if (!ds.inSameComponent(edge.u, edge.v)) {
                ds.union(edge.u, edge.v);
                mst.add(edge);
            }
        }
        return mst;
    }

    private static <T> List<Edge<T>> getEdges(Map<T, List<Edge<T>>> graph) {
        List<Edge<T>> edges = new ArrayList<>();
        for (T node : graph.keySet()) {
            edges.addAll(graph.get(node));
        }
        return edges;
    }
}
