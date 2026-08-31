package Graphs.G51;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static List<Integer> findNumIslands(List<List<Integer>> mtx, List<List<Integer>> cells) {
        int n = mtx.size(), m = mtx.getFirst().size();
        List<Integer> nodes = getNodes(cells);
        List<Integer> result = new ArrayList<>();
        DisjointSet<Integer> disjointSet = new DisjointSet<>(nodes);
        for (List<Integer> cell : cells) {
            int i = cell.getFirst(), j = cell.getLast();
            mtx.get(i).set(j, 1);
            Integer node = getNeighbourNodeWhichIsAnIsland(i, j);
            if (node != null) {
                disjointSet.union(node, getNode(cell));
            }
            result.add(disjointSet.getNumberOfComponents());
        }
        return result;
    }
}
