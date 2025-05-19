package BinarySearch.BS27;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getMedianFromMatrix(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        MinHeap<HeapElement> minHeap = new MinHeap<>();
        for (int i = 0; i < n; i += 1) {
            minHeap.insert(new HeapElement(mtx.get(i).getFirst(), i, 0));
        }
        int medianIndex = (n * m)/2;
        int counter = -1;
        while (counter != medianIndex) {
            HeapElement heapElement = minHeap.pop();
            counter += 1;
            if (counter == medianIndex) {
                return heapElement.getValue();
            }
            int colIndex = heapElement.getCol();
            if (0 <= colIndex + 1 && colIndex + 1 < m) {
                minHeap.insert(new HeapElement(mtx.get(heapElement.getRow()).get(colIndex + 1), heapElement.getRow(), colIndex + 1));
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        // Example 1
        System.out.println(
                getMedianFromMatrix(
                        Arrays.asList(
                                Arrays.asList(1, 3, 5),
                                Arrays.asList(2, 6, 9),
                                Arrays.asList(3, 6, 9)
                        )
                )
        );

        // Example 2
        System.out.println(
                getMedianFromMatrix(
                        Arrays.asList(
                                Arrays.asList(1),
                                Arrays.asList(2),
                                Arrays.asList(3)
                        )
                )
        );

        // Example 3
        System.out.println(
                getMedianFromMatrix(
                        Arrays.asList(
                                Arrays.asList(3),
                                Arrays.asList(5),
                                Arrays.asList(8)
                        )
                )
        );
    }
}
