package Graphs.G51;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class Solution {
    public static List<Integer> findNumIslands(Integer n, Integer m, List<List<Integer>> cells) {
        List<List<Integer>> mtx = getMtx(n, m);
        List<Integer> nodes = getNodes(cells, m);
        List<Integer> result = new ArrayList<>();
        DisjointSet<Integer> disjointSet = new DisjointSet<>(nodes);
        for (List<Integer> cell : cells) {
            int i = cell.getFirst(), j = cell.getLast();
            mtx.get(i).set(j, 1);
            Integer node = getNeighbourNodeWhichIsAnIsland(i, j, n, m, mtx);
            if (node != null) {
                disjointSet.union(node, getNode(cell, m));
            }
            result.add(getNumIslandsFromDSU(disjointSet, mtx, m));
        }
        return result;
    }

    private static Integer getNumIslandsFromDSU(DisjointSet<Integer> disjointSet, List<List<Integer>> mtx, int m) {
        int count = 0;
        for (Integer node : disjointSet.parents.keySet()) {
            if (Objects.equals(disjointSet.parents.get(node), node) && mtx.get(node / m).get(node % m) == 1) {
                count += 1;
            }
        }
        return count;
    }

    private static List<List<Integer>> getMtx(Integer n, Integer m) {
        List<List<Integer>> mtx = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(0);
            }
            mtx.add(row);
        }
        return mtx;
    }

    private static Integer getNeighbourNodeWhichIsAnIsland(int i, int j, int n, int m, List<List<Integer>> mtx) {
        if (0 <= i - 1 && i - 1 < n && mtx.get(i - 1).get(j) == 1) {
            return getNode(List.of(i - 1, j), m);
        } else if (0 <= j + 1 && j + 1 < m && mtx.get(i).get(j + 1) == 1) {
            return getNode(List.of(i, j + 1), m);
        } else if (0 <= i + 1 && i + 1 < n && mtx.get(i + 1).get(j) == 1) {
            return getNode(List.of(i + 1, j), m);
        } else if (0 <= j - 1 && j - 1 < m && mtx.get(i).get(j - 1) == 1) {
            return getNode(List.of(i, j - 1), m);
        }
        return null;
    }

    private static Integer getNode(List<Integer> cell, int m) {
        return cell.getFirst() * m + cell.getLast();
    }

    private static List<Integer> getNodes(List<List<Integer>> cells, int m) {
        List<Integer> nodes = new ArrayList<>();
        for (List<Integer> cell : cells) {
            nodes.add(getNode(cell, m));
        }
        return nodes;
    }

    public static void main(String[] args) {
        System.out.println(
                findNumIslands(
                        4, 5,
                        Arrays.asList(
                                Arrays.asList(1, 1),
                                Arrays.asList(0, 1),
                                Arrays.asList(3, 3),
                                Arrays.asList(3, 4)
                        )
                )
        );
    }
}
