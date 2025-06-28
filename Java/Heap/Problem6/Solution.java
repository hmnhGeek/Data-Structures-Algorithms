package Heap.Problem6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        List<List<Integer>> matrix1 = Arrays.asList(
                Arrays.asList(1, 2, 3),
                Arrays.asList(4, 5, 6),
                Arrays.asList(7, 8, 9)
        );
        System.out.println(merge(matrix1));

        // Example 2
        List<List<Integer>> matrix2 = Arrays.asList(
                Arrays.asList(1, 2, 3, 4),
                Arrays.asList(2, 2, 3, 4),
                Arrays.asList(5, 5, 6, 6),
                Arrays.asList(7, 8, 9, 9)
        );
        System.out.println(merge(matrix2));
    }

    public static <T extends Comparable<T>> List<T> merge(List<List<T>> matrix) {
        int n = matrix.size(), m = matrix.getFirst().size();
        MinHeap<HeapElement<T>> minHeap = new MinHeap<>();
        for (int i = 0; i < n; i += 1) {
            minHeap.insert(new HeapElement<>(matrix.get(i).getFirst(), i, 0));
        }
        List<T> result = new ArrayList<>();
        while (!minHeap.isEmpty()) {
            HeapElement<T> poppedElement = minHeap.pop();
            result.add(poppedElement.getData());
            if (0 <= poppedElement.getColIndex() + 1 && poppedElement.getColIndex() + 1 < m) {
                minHeap.insert(new HeapElement<>(matrix.get(poppedElement.getRowIndex()).get(poppedElement.getColIndex() + 1), poppedElement.getRowIndex(), poppedElement.getColIndex() + 1));
            }
        }
        return result;
    }
}
