// Problem link - https://www.geeksforgeeks.org/problems/maximum-connected-group/1
// Solution - https://www.youtube.com/watch?v=lgiz0Oup6gM&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=52


package Graphs.G52;

import java.util.*;

public class Solution {
    public static Integer getLargestIsland(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm) and space complexity is O(nm).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        List<Integer> nodes = getNodes(mtx, n, m);
        DisjointSet<Integer> disjointSet = new DisjointSet<>(nodes);
        unionizeExistingIslands(mtx, n, m, disjointSet);
        Integer largest = Collections.max(disjointSet.size.values());
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (mtx.get(i).get(j) == 0) {
                    Set<Integer> ulp = new HashSet<>();
                    List<List<Integer>> neighbours = getNeighbours(mtx, i, j, n, m);
                    for (List<Integer> neighbour : neighbours) {
                        int x = neighbour.getFirst(), y = neighbour.getLast();
                        Integer adjNode = (x * m) + y;
                        ulp.add(disjointSet.findUltimateParent(adjNode));
                    }
                    int currSize = 0;
                    for (Integer parent : ulp) {
                        currSize += disjointSet.size.get(parent);
                    }
                    currSize += 1;
                    largest = Math.max(largest, currSize);
                }
            }
        }
        return largest;
    }

    private static void unionizeExistingIslands(List<List<Integer>> mtx, int n, int m, DisjointSet<Integer> disjointSet) {
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (mtx.get(i).get(j) == 1) {
                    Integer node = (i * m) + j;
                    List<List<Integer>> neighbours = getNeighbours(mtx, i, j, n, m);
                    for (List<Integer> neighbour : neighbours) {
                        int x = neighbour.getFirst(), y = neighbour.getLast();
                        Integer adjNode = (x * m) + y;
                        disjointSet.union(node, adjNode);
                    }
                }
            }
        }
    }

    private static List<List<Integer>> getNeighbours(List<List<Integer>> mtx, int i, int j, int n, int m) {
        List<List<Integer>> neighbours = new ArrayList<>();
        if (0 <= i - 1 && i - 1 < n && mtx.get(i - 1).get(j) == 1) {
            neighbours.add(List.of(i - 1, j));
        }
        if (0 <= j + 1 && j + 1 < m && mtx.get(i).get(j + 1) == 1) {
            neighbours.add(List.of(i, j + 1));
        }
        if (0 <= i + 1 && i + 1 < n && mtx.get(i + 1).get(j) == 1) {
            neighbours.add(List.of(i + 1, j));
        }
        if (0 <= j - 1 && j - 1 < m && mtx.get(i).get(j - 1) == 1) {
            neighbours.add(List.of(i, j - 1));
        }
        return neighbours;
    }

    private static List<Integer> getNodes(List<List<Integer>> mtx, int n, int m) {
        List<Integer> nodes = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (mtx.get(i).get(j) == 1) {
                    nodes.add((m * i) + j);
                }
            }
        }
        return nodes;
    }

    public static void main(String[] args) {
        System.out.println(
                getLargestIsland(
                        List.of(
                                List.of(1, 1),
                                List.of(0, 1)
                        )
                )
        );

        System.out.println(
                getLargestIsland(
                        List.of(
                                List.of(1, 0, 1),
                                List.of(1, 0, 1),
                                List.of(1, 0, 1)
                        )
                )
        );

        System.out.println(
                getLargestIsland(
                        List.of(
                                List.of(1, 1, 0, 1, 1),
                                List.of(1, 1, 0, 1, 1),
                                List.of(1, 1, 0, 1, 1),
                                List.of(0, 0, 1, 0, 0),
                                List.of(0, 0, 1, 1, 1),
                                List.of(0, 0, 1, 1, 1)
                        )
                )
        );

        System.out.println(
                getLargestIsland(
                        List.of(
                                List.of(1, 0, 1, 1, 0),
                                List.of(1, 0, 0, 1, 0),
                                List.of(0, 1, 1, 0, 1),
                                List.of(1, 0, 1, 0, 1),
                                List.of(0, 1, 0, 1, 0)
                        )
                )
        );

        System.out.println(
                getLargestIsland(
                        List.of(
                                List.of(1, 1),
                                List.of(1, 1)
                        )
                )
        );
    }
}
