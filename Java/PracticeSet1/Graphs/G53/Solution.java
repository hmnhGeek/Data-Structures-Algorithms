package PracticeSet1.Graphs.G53;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static Integer removeStones(List<List<Integer>> stones) {
        List<Integer> dimensions = getMaxDimensions(stones);
        DisjointSet<Integer> disjointSet = getDisjointSet(stones, dimensions);
        int maxCol = dimensions.getLast();
        for (List<Integer> coordinate : stones) {
            Integer node1 = coordinate.getLast();
            Integer node2 = coordinate.getFirst() + maxCol + 1;
            disjointSet.union(node1, node2);
        }
        int validComponents = getValidComponents(disjointSet);
        return stones.size() - validComponents;
    }

    private static int getValidComponents(DisjointSet<Integer> disjointSet) {
        int count = 0;
        for (Integer node : disjointSet.parent.keySet()) {
            if (node.equals(disjointSet.parent.get(node)) && disjointSet.size.get(node) > 1) {
                count += 1;
            }
        }
        return count;
    }

    private static DisjointSet<Integer> getDisjointSet(List<List<Integer>> stones, List<Integer> dimensions) {
        List<Integer> nodes = new ArrayList<>();
        int maxRow = dimensions.getFirst();
        int maxCol = dimensions.getLast();
        for (int j = 0; j <= maxCol; j += 1) {
            nodes.add(j);
        }
        for (int i = 0; i <= maxRow; i += 1) {
            nodes.add(i + maxCol + 1);
        }
        DisjointSet<Integer> disjointSet = new DisjointSet<>(nodes);
        return disjointSet;
    }

    private static List<Integer> getMaxDimensions(List<List<Integer>> stones) {
        int maxRow = Integer.MIN_VALUE, maxCol = Integer.MIN_VALUE;
        for (List<Integer> coordinate : stones) {
            maxRow = Math.max(maxRow, coordinate.getFirst());
            maxCol = Math.max(maxCol, coordinate.getLast());
        }
        return List.of(maxRow, maxCol);
    }

    public static void main(String[] args) {
        System.out.println(Solution.removeStones(List.of(
                List.of(0, 0),
                List.of(0, 1),
                List.of(1, 0),
                List.of(1, 2),
                List.of(2, 1),
                List.of(2, 2)
        )));

        System.out.println(Solution.removeStones(List.of(
                List.of(0, 0),
                List.of(0, 2),
                List.of(1, 1),
                List.of(2, 0),
                List.of(2, 2)
        )));

        System.out.println(Solution.removeStones(List.of(
                List.of(0, 0)
        )));

        System.out.println(Solution.removeStones(List.of(
                List.of(0, 1),
                List.of(1, 0),
                List.of(0, 0)
        )));

        System.out.println(Solution.removeStones(List.of(
                List.of(2, 0),
                List.of(2, 1),
                List.of(3, 1),
                List.of(3, 2),
                List.of(5, 5)
        )));

    }
}
