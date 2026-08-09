// Problem link - https://www.geeksforgeeks.org/problems/connecting-the-graph/1
// Solution - https://www.youtube.com/watch?v=FYrl7iz9_ZU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=49


package Graphs.G49;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static Integer getMinOps(List<List<Integer>> edges, int n) {
        /*
            Time complexity is O(n + E) and space complexity is O(n).
         */
        List<Integer> nodes = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            nodes.add(i);
        }
        DisjointSet<Integer> disjointSet = new DisjointSet<>(nodes);
        int extraEdgesCount = 0;
        for (List<Integer> edge : edges) {
            Integer node1 = edge.getFirst(), node2 = edge.getLast();
            if (disjointSet.inSameComponent(node1, node2)) {
                extraEdgesCount += 1;
            } else {
                disjointSet.union(node1, node2);
            }
        }
        if (extraEdgesCount >= disjointSet.getNumComponents() - 1) {
            return disjointSet.getNumComponents() - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.getMinOps(
                        List.of(
                                List.of(0, 1),
                                List.of(0, 2),
                                List.of(1, 2)
                        ),
                        4
                )
        );

        System.out.println(
                Solution.getMinOps(
                        List.of(
                                List.of(0, 1),
                                List.of(0, 2),
                                List.of(0, 3),
                                List.of(1, 2),
                                List.of(1, 3)
                        ),
                        6
                )
        );

        System.out.println(
                Solution.getMinOps(
                        List.of(
                                List.of(0, 1),
                                List.of(0, 2),
                                List.of(0, 3),
                                List.of(1, 2)
                        ),
                        6
                )
        );
    }
}
