// Problem link - https://www.geeksforgeeks.org/problems/kth-element-in-matrix/1


package PracticeSet2.Matrix.Problem9;

import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                Solution.getKthSmallest(
                        List.of(
                                List.of(16, 28, 60, 64),
                                List.of(22, 41, 63, 91),
                                List.of(27, 50, 87, 93),
                                List.of(36, 78, 87, 94)
                        ),
                        3
                )
        );

        System.out.println(
                Solution.getKthSmallest(
                        List.of(
                                List.of(16, 28, 60, 64),
                                List.of(22, 41, 63, 91),
                                List.of(27, 50, 87, 93),
                                List.of(36, 78, 87, 94)
                        ),
                        100
                )
        );

        System.out.println(
                Solution.getKthSmallest(
                        List.of(
                                List.of(16, 28, 60, 64),
                                List.of(22, 41, 63, 91),
                                List.of(27, 50, 87, 93),
                                List.of(36, 78, 87, 94)
                        ),
                        -10
                )
        );

        System.out.println(
                Solution.getKthSmallest(
                        List.of(
                                List.of(10, 20, 30, 40),
                                List.of(15, 25, 35, 45),
                                List.of(24, 29, 37, 48),
                                List.of(32, 33, 39, 50)
                        ),
                        7
                )
        );

        System.out.println(
                Solution.getKthSmallest(
                        List.of(
                                List.of(10, 20, 30, 40),
                                List.of(15, 25, 35, 45),
                                List.of(24, 29, 37, 48),
                                List.of(32, 33, 39, 50)
                        ),
                        15
                )
        );
    }

    public static Integer getKthSmallest(List<List<Integer>> mtx, Integer k) {
        /*
            Time complexity is O({n + k} * log(n)) time and space complexity is O(n).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        MinHeap<HeapElement<Integer>> pq = new MinHeap<>();
        initiateMinHeap(mtx, n, pq);
        int counter = 0;
        while (!pq.isEmpty()) {
            HeapElement<Integer> heapElement = pq.pop();
            counter += 1;
            if (counter == k) return heapElement.data;
            int x = heapElement.i, y = heapElement.j;
            if (0 < y + 1 && y + 1 < m) {
                pq.insert(new HeapElement<>(mtx.get(x).get(y + 1), x, y + 1));
            }
        }
        return null;
    }

    private static void initiateMinHeap(List<List<Integer>> mtx, int n, MinHeap<HeapElement<Integer>> pq) {
        for (int i = 0; i < n; i += 1) {
            pq.insert(new HeapElement<>(mtx.get(i).getFirst(), i, 0));
        }
    }
}
