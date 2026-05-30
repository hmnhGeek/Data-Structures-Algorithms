// Problem link - https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1


package PracticeSet1.BinarySearch.BS27;

import java.util.Arrays;
import java.util.List;

public class Solution {
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

    public static Integer getMedianFromMatrix(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm * log(n)) and space complexity is O(n).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        int totalIntegers = n*m;
        MinHeap<HeapElement<Integer>> pq = new MinHeap<>();
        for (int i = 0; i < n; i += 1) {
            pq.insert(new HeapElement<>(mtx.get(i).getFirst(), i, 0));
        }
        int counter = 0;
        while (!pq.isEmpty()) {
            HeapElement<Integer> heapElement = pq.pop();
            counter += 1;
            if (counter == (totalIntegers/2) + 1) {
                return heapElement.data;
            }
            if (0 <= heapElement.j + 1 && heapElement.j + 1 < m) {
                pq.insert(
                        new HeapElement<>(
                                mtx.get(heapElement.i).get(heapElement.j + 1),
                                heapElement.i,
                                heapElement.j + 1
                        )
                );
            }
        }
        return null;
    }
}
