// Problem link - https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/#floyd-warshall-algorithm
// Solution - https://www.youtube.com/watch?v=YbY8cVwWAvw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=42


package Graphs.G42;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {

        Map<Integer, List<AdjacentNode<Integer>>> graph1 = Map.of(
                0, List.of(new AdjacentNode<>(1, 2)),
                1, List.of(
                        new AdjacentNode<>(0, 1),
                        new AdjacentNode<>(2, 3)
                ),
                2, List.of(),
                3, List.of(
                        new AdjacentNode<>(0, 3),
                        new AdjacentNode<>(1, 5),
                        new AdjacentNode<>(2, 4)
                )
        );

        Map<Integer, List<AdjacentNode<Integer>>> graph2 = Map.of(
                0, List.of(
                        new AdjacentNode<>(1, 1),
                        new AdjacentNode<>(2, 43)
                ),
                1, List.of(
                        new AdjacentNode<>(0, 1),
                        new AdjacentNode<>(2, 6)
                ),
                2, List.of()
        );

        Map<Integer, List<AdjacentNode<Integer>>> graph3 = Map.of(
                0, List.of(new AdjacentNode<>(1, 25)),
                1, List.of()
        );

        Map<Integer, List<AdjacentNode<Integer>>> graph4 = Map.of(
                0, List.of(
                        new AdjacentNode<>(1, 4),
                        new AdjacentNode<>(3, 5)
                ),
                1, List.of(
                        new AdjacentNode<>(2, 1),
                        new AdjacentNode<>(4, 6)
                ),
                2, List.of(
                        new AdjacentNode<>(0, 2),
                        new AdjacentNode<>(3, 3)
                ),
                3, List.of(
                        new AdjacentNode<>(2, 1),
                        new AdjacentNode<>(4, 2)
                ),
                4, List.of(
                        new AdjacentNode<>(0, 1),
                        new AdjacentNode<>(3, 4)
                )
        );

        System.out.println(getShortestPaths(graph1));
        System.out.println(getShortestPaths(graph2));
        System.out.println(getShortestPaths(graph3));
        System.out.println(getShortestPaths(graph4));
    }

    public static List<List<Integer>> getShortestPaths(Map<Integer, List<AdjacentNode<Integer>>> graph) {
        /*
            Time complexity is O(V^3) and space complexity is O(V^2).
         */
        List<List<Integer>> costMatrix = getCostMatrix(graph);
        int n = graph.size();
        for (int k = 0; k < n; k += 1) {
            for (int i = 0; i < n; i += 1) {
                for (int j = 0; j < n; j += 1) {
                    if ( costMatrix.get(i).get(k) != Integer.MAX_VALUE && costMatrix.get(k).get(j) != Integer.MAX_VALUE &&
                            costMatrix.get(i).get(k) + costMatrix.get(k).get(j) < costMatrix.get(i).get(j)) {
                        costMatrix.get(i).set(j, costMatrix.get(i).get(k) + costMatrix.get(k).get(j));
                    }
                }
            }
        }

        for (int i = 0; i < n; i += 1) {
            if (costMatrix.get(i).get(i) < 0) return null;
        }

        return costMatrix;
    }

    private static <T> List<List<Integer>> getCostMatrix(Map<Integer, List<AdjacentNode<Integer>>> graph) {
        List<List<Integer>> costMatrix = new ArrayList<>();
        int n = graph.size();
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j += 1) {
                if (i == j) {
                    row.add(0);
                    continue;
                }
                row.add(Integer.MAX_VALUE);
            }
            costMatrix.add(row);
        }
        for (Integer node : graph.keySet()) {
            for (AdjacentNode<Integer> adjacentNode : graph.get(node)) {
                costMatrix.get(node).set(adjacentNode.node, adjacentNode.edgeWeight);
            }
        }
        return costMatrix;
    }
}
