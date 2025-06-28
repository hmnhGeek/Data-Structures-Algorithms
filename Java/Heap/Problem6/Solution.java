// Problem Link - https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1

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
        /*
            Time complexity is thus O(n*m*log(n)) and space complexity is O(n).
         */
        int n = matrix.size(), m = matrix.getFirst().size();
        MinHeap<HeapElement<T>> minHeap = new MinHeap<>();

        // This will take O(n * log(n)) time and O(n) space.
        for (int i = 0; i < n; i += 1) {
            minHeap.insert(new HeapElement<>(matrix.get(i).getFirst(), i, 0));
        }
        List<T> result = new ArrayList<>();

        // this loop will run for nm times, i.e, for all elements of the matrix.
        while (!minHeap.isEmpty()) {
            // This will take O(log(n)) time.
            HeapElement<T> poppedElement = minHeap.pop();
            result.add(poppedElement.getData());

            // This will again take O(log(n)) time.
            if (0 <= poppedElement.getColIndex() + 1 && poppedElement.getColIndex() + 1 < m) {
                minHeap.insert(new HeapElement<>(matrix.get(poppedElement.getRowIndex()).get(poppedElement.getColIndex() + 1), poppedElement.getRowIndex(), poppedElement.getColIndex() + 1));
            }
        }
        return result;
    }
}
