package Graphs.G48;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static Integer getNumProvinces(List<List<Integer>> graph) {
        int n = graph.size();
        List<Integer> nodes = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            nodes.add(i);
        }
        DisjointSet<Integer> disjointSet = new DisjointSet<>(nodes);
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < n; j += 1) {
                if (i == j) continue;
                if (graph.get(i).get(j).equals(1)) {
                    disjointSet.union(i, j);
                }
            }
        }
        return disjointSet.getNumComponents();
    }

    public static void main(String[] args) {

        System.out.println(
                Solution.getNumProvinces(
                        List.of(
                                List.of(0, 1, 0, 0, 0, 0, 0),
                                List.of(1, 0, 1, 0, 0, 0, 0),
                                List.of(0, 1, 0, 0, 0, 0, 0),
                                List.of(0, 0, 0, 0, 1, 0, 0),
                                List.of(0, 0, 0, 1, 0, 0, 0),
                                List.of(0, 0, 0, 0, 0, 0, 1),
                                List.of(0, 0, 0, 0, 0, 1, 0)
                        )
                )
        );

        System.out.println(
                Solution.getNumProvinces(
                        List.of(
                                List.of(1, 0, 1),
                                List.of(0, 1, 0),
                                List.of(1, 0, 1)
                        )
                )
        );

        System.out.println(
                Solution.getNumProvinces(
                        List.of(
                                List.of(1, 1),
                                List.of(1, 1)
                        )
                )
        );

        System.out.println(
                Solution.getNumProvinces(
                        List.of(
                                List.of(1, 0, 0),
                                List.of(0, 1, 0),
                                List.of(0, 0, 1)
                        )
                )
        );

        System.out.println(
                Solution.getNumProvinces(
                        List.of(
                                List.of(1, 1, 1, 0),
                                List.of(1, 1, 1, 0),
                                List.of(1, 1, 1, 0),
                                List.of(0, 0, 0, 1)
                        )
                )
        );
    }
}
