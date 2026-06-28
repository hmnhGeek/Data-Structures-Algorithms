package Graphs.G43;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Solution {
    public static List<List<Integer>> findDistances(Map<Integer, List<List<Integer>>> graph, Integer threshold) {
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
}
