package Graphs.G43;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static List<List<Integer>> findDistances(Map<Integer, List<List<Integer>>> graph) {
        List<List<Integer>> adjMatrix = getMatrixGraph(graph);

        for (Integer k : graph.keySet()) {
            for (int i = 0; i < graph.size(); i += 1) {
                for (int j = 0; j < graph.size(); j += 1) {
                    if (adjMatrix.get(i).get(k) != Integer.MAX_VALUE && adjMatrix.get(k).get(j) != Integer.MAX_VALUE &&
                            adjMatrix.get(i).get(k) + adjMatrix.get(k).get(j) < adjMatrix.get(i).get(j)) {
                        adjMatrix.get(i).set(j, adjMatrix.get(i).get(k) + adjMatrix.get(k).get(j));
                    }
                }
            }
        }
        for (int i = 0; i < graph.size(); i += 1) {
            if (adjMatrix.get(i).get(i) < 0) return null;
        }
        return adjMatrix;
    }

    private static List<List<Integer>> getMatrixGraph(Map<Integer, List<List<Integer>>> graph) {
        List<List<Integer>> mtx = new ArrayList<>();
        for (int i = 0; i < graph.size(); i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < graph.size(); j += 1) {
                if (i == j) {
                    row.add(0);
                    continue;
                }
                row.add(Integer.MAX_VALUE);
            }
            mtx.add(row);
        }

        for (Integer node : graph.keySet()) {
            for (List<Integer> adj : graph.get(node)) {
                mtx.get(node).set(adj.getFirst(), adj.getLast());
            }
        }
        return mtx;
    }

    public static Integer findCity(Map<Integer, List<List<Integer>>> graph, Integer threshold) {
        List<List<Integer>> adjMtx = findDistances(graph);
        int city = -1;
        int minReachable = graph.size();
        for (int i = 0; i < graph.size(); i += 1) {
            int count = 0;
            for (int j = 0; j < graph.size(); j += 1) {
                if (adjMtx.get(i).get(j) <= threshold) {
                    count += 1;
                }
            }
            if (count <= minReachable) {
                minReachable = count;
                city = i;
            }
        }
        return city;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.findCity(
                        buildGraph(
                                new int[][]{
                                        {0, 1, 3},
                                        {1, 2, 1},
                                        {1, 3, 4},
                                        {2, 3, 1}
                                },
                                4
                        ),
                        4
                )
        );

        System.out.println(
                Solution.findCity(
                        buildGraph(
                                new int[][]{
                                        {0, 1, 2},
                                        {0, 4, 8},
                                        {1, 2, 3},
                                        {1, 4, 2},
                                        {2, 3, 1},
                                        {3, 4, 1}
                                },
                                5
                        ),
                        2
                )
        );
    }

    private static Map<Integer, List<List<Integer>>> buildGraph(int[][] edges, int n) {
        Map<Integer, List<List<Integer>>> graph = new HashMap<>();

        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int[] edge : edges) {
            graph.get(edge[0]).add(List.of(edge[1], edge[2]));
            graph.get(edge[1]).add(List.of(edge[0], edge[2]));
        }

        return graph;
    }
}
