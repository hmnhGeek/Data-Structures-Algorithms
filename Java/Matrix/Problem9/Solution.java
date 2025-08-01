package Matrix.Problem9;

import Matrix.Problem9.Heap.MinHeap;
import Matrix.Problem9.HeapElement.HeapElement;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static <T extends Comparable<T>> T getMin(List<List<T>> mtx, Integer k) {
        MinHeap<HeapElement<T>> minHeap = new MinHeap<>();
        int n = mtx.size(), m = mtx.getFirst().size();
        for (int i = 0; i < n; i += 1) {
            minHeap.insert(new HeapElement<>(mtx.get(i).getFirst(), i, 0));
        }
        int counter = 0;
        while (!minHeap.isEmpty()) {
            HeapElement<T> heapElement = minHeap.pop();
            counter += 1;
            if (counter == k) {
                return heapElement.getData();
            }
            Integer y = heapElement.getJ();
            Integer x = heapElement.getI();
            if (0 <= y + 1 && y + 1 < m) {
                minHeap.insert(new HeapElement<>(mtx.get(x).get(y + 1), x, y + 1));
            }
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(
                getMin(
                        Arrays.asList(
                                Arrays.asList(16, 28, 60, 64),
                                Arrays.asList(22, 41, 63, 91),
                                Arrays.asList(27, 50, 87, 93),
                                Arrays.asList(36, 78, 87, 94)
                        ),
                        3
                )
        );

        System.out.println(
                getMin(
                        Arrays.asList(
                                Arrays.asList(10, 20, 30, 40),
                                Arrays.asList(15, 25, 35, 45),
                                Arrays.asList(24, 29, 37, 48),
                                Arrays.asList(32, 33, 39, 50)
                        ),
                        7
                )
        );
    }
}
