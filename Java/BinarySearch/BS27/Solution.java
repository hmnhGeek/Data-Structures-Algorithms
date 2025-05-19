package BinarySearch.BS27;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getMedianFromMatrix(List<List<Integer>> mtx) {
        // get the dimensions of the matrix.
        int n = mtx.size(), m = mtx.getFirst().size();

        // push the first column into the min heap.
        MinHeap<HeapElement> minHeap = new MinHeap<>();
        for (int i = 0; i < n; i += 1) {
            minHeap.insert(new HeapElement(mtx.get(i).getFirst(), i, 0));
        }

        // get the median index
        int medianIndex = (n * m)/2;

        // define a counter which will keep track of the median index (when to stop).
        int counter = -1;

        // while the counter has not reached the median element. This will run for O(nm/2) time.
        while (counter != medianIndex) {
            // get the smallest element in O(log(n)) time & increment the counter value.
            HeapElement heapElement = minHeap.pop();
            counter += 1;

            // if counter reached median index, return the median value.
            if (counter == medianIndex) {
                return heapElement.getValue();
            }

            // if the next element to the popped element is available, then push it into the min heap in
            // O(log(n)) time.
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
