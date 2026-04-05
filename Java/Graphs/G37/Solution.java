package Graphs.G37;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static Integer getMinimumEffort(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        MinHeap<HeapElement<Integer>> pq = new MinHeap<>();
        List<List<Integer>> distances = getDistancesMtx(n, m);
        pq.insert(new HeapElement<>(distances.getFirst().getFirst(), 0, 0));
        while (!pq.isEmpty()) {
            HeapElement<Integer> heapElement = pq.pop();
            Integer diff = heapElement.data;
            Integer i = heapElement.i, j = heapElement.j;
            if (i == n - 1 && j == m - 1) return diff;
            List<List<Integer>> neighbours = getNeighbours(mtx, i, j, n, m);
            for (List<Integer> neighbour : neighbours) {
                int x = neighbour.getFirst(), y = neighbour.getLast();
                int effort = Math.abs(mtx.get(x).get(y) - mtx.get(i).get(j));
                int newEffort = Math.max(effort, diff);
                if (distances.get(x).get(y) > newEffort) {
                    distances.get(x).set(y, newEffort);
                    pq.insert(new HeapElement<>(newEffort, x, y));
                }
            }
        }
        return null;
    }

    private static List<List<Integer>> getNeighbours(List<List<Integer>> mtx, Integer i, Integer j, int n, int m) {
        List<List<Integer>> neighbours = new ArrayList<>();

        if (0 <= i - 1 && i - 1 < n) {
            neighbours.add(List.of(i - 1, j));
        }
        if (0 <= j + 1 && j + 1 < m) {
            neighbours.add(List.of(i, j + 1));
        }
        if (0 <= i + 1 && i + 1 < n) {
            neighbours.add(List.of(i + 1, j));
        }
        if (0 <= j - 1 && j - 1 < m) {
            neighbours.add(List.of(i, j - 1));
        }
        return neighbours;
    }

    private static List<List<Integer>> getDistancesMtx(int n, int m) {
        List<List<Integer>> mtx = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(Integer.MAX_VALUE);
            }
            mtx.add(row);
        }
        mtx.getFirst().set(0, 0);
        return mtx;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.getMinimumEffort(
                        List.of(
                                List.of(1, 2, 2),
                                List.of(3, 8, 2),
                                List.of(5, 3, 5)
                        )
                )
        );

        System.out.println(
                Solution.getMinimumEffort(
                        List.of(
                                List.of(7, 7),
                                List.of(7, 7)
                        )
                )
        );

        System.out.println(
                Solution.getMinimumEffort(
                        List.of(
                                List.of(1, 2, 3),
                                List.of(3, 8, 4),
                                List.of(5, 3, 5)
                        )
                )
        );

        System.out.println(
                Solution.getMinimumEffort(
                        List.of(
                                List.of(1, 2, 1, 1, 1),
                                List.of(1, 2, 1, 2, 1),
                                List.of(1, 2, 1, 2, 1),
                                List.of(1, 2, 1, 2, 1),
                                List.of(1, 1, 1, 2, 1)
                        )
                )
        );

        System.out.println(
                Solution.getMinimumEffort(
                        List.of(
                                List.of(1, 8, 8),
                                List.of(3, 8, 9),
                                List.of(5, 3, 5)
                        )
                )
        );

        System.out.println(
                Solution.getMinimumEffort(
                        List.of(
                                List.of(1, 3, 1),
                                List.of(9, 9, 3),
                                List.of(9, 9, 1)
                        )
                )
        );
    }
}
