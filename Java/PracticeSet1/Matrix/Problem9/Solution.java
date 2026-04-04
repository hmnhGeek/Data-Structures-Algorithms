// Problem link - https://www.geeksforgeeks.org/problems/kth-element-in-matrix/1


package PracticeSet1.Matrix.Problem9;

import java.util.List;


class HeapElement<T extends Comparable<T>> implements Comparable<HeapElement<T>> {
    public T data;
    public Integer i, j;

    public HeapElement(T data, Integer i, Integer j) {
        this.data = data;
        this.i = i;
        this.j = j;
    }

    @Override
    public int compareTo(HeapElement<T> o) {
        return this.data.compareTo(o.data);
    }
}


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

        if (k <= 0 || k >= mtx.size() * mtx.getFirst().size()) return null;
        MinHeap<HeapElement<Integer>> pq = new MinHeap<>();

        // this will take O(n * log(n)) time.
        pushFirstRowInPQ(mtx, pq);
        int counter = 1;

        // this will take O(k * log(n)) time.
        while (counter != k) {
            HeapElement<Integer> heapElement = pq.pop();
            counter += 1;
            if (0 <= heapElement.j + 1 && heapElement.j + 1 < mtx.getFirst().size()) {
                pq.insert(new HeapElement<>(
                        mtx.get(heapElement.i).get(heapElement.j + 1),
                        heapElement.i,
                        heapElement.j + 1
                ));
            }
        }
        return pq.pop().data;
    }

    private static void pushFirstRowInPQ(List<List<Integer>> mtx, MinHeap<HeapElement<Integer>> pq) {
        for (int i = 0; i < mtx.size(); i += 1) {
            pq.insert(new HeapElement<>(mtx.get(i).getFirst(), i, 0));
        }
    }
}
