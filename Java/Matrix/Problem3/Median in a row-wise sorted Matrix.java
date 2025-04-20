// Problem link - https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1


package Matrix.Problem3;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class MinHeap<T extends Comparable<T>> implements Heap<T> {
    private List<T> heap;

    public MinHeap() {
        this.heap = new ArrayList<>();
    }

    @Override
    public List<T> getHeap() {
        return this.heap;
    }

    @Override
    public Integer getChildIndex(Integer lci, Integer rci) {
        if (lci == null && rci == null) {
            return null;
        }
        if (lci == null) {
            return rci;
        }
        if (rci == null) {
            return lci;
        }
        Integer minChildIndex = lci;
        if (this.heap.get(rci).compareTo(this.heap.get(lci)) < 0) {
            minChildIndex = rci;
        }
        return minChildIndex;
    }

    @Override
    public void heapifyUp(Integer startIndex) {
        if (startIndex.equals(0)) {
            return;
        }
        Integer pi = getPi(startIndex);
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer minChildIndex = getChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (this.heap.get(pi).compareTo(this.heap.get(minChildIndex)) > 0) {
                Collections.swap(this.heap, pi, minChildIndex);
            }
            heapifyUp(pi);
        }
    }

    @Override
    public void heapifyDown(Integer pi) {
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer minChildIndex = getChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (this.heap.get(pi).compareTo(this.heap.get(minChildIndex)) > 0) {
                Collections.swap(this.heap, pi, minChildIndex);
            }
            heapifyDown(minChildIndex);
        }
    }
}


// Implementing a Comparable is required because MinHeap<T> expects a T which is comparable. So even though,
// T in HeapElement in Comparable, the HeapElement itself needs to define a natural sorting logic for it to
// be used inside MinHeap class.
class HeapElement<T extends Comparable<T>> implements Comparable<HeapElement<T>> {
    private final T value;
    private final Integer rowIndex;
    private final Integer colIndex;

    public HeapElement(T value, Integer rowIndex, Integer colIndex) {
        this.value = value;
        this.rowIndex = rowIndex;
        this.colIndex = colIndex;
    }

    public T getValue() {
        return value;
    }

    public Integer getRowIndex() {
        return rowIndex;
    }

    public Integer getColIndex() {
        return colIndex;
    }

    @Override
    public String toString() {
        return String.format("Element = %s, i = %d, j = %d", getValue(), getRowIndex(), getColIndex());
    }

    @Override
    public int compareTo(HeapElement<T> o) {
        return getValue().compareTo(o.getValue());
    }
}


class Solution {
    public static Integer getMedianFromMatrix(List<List<Integer>> matrix) {
        /*
            Time complexity is O(nm * log(n)) and space complexity is O(nm).
         */

        // get the dimensions of the matrix.
        Integer n = matrix.size(), m = matrix.getFirst().size();

        // get the median index
        Integer medianIndex = (n * m)/2;

        // define a new min heap which will store O(nm/2) elements.
        MinHeap<HeapElement<Integer>> minHeap = new MinHeap<>();

        // in O(n * log(n * log(n)) time, insert the first column into the min heap.
        for (int i = 0; i < n; i += 1) {
            minHeap.insert(new HeapElement<>(matrix.get(i).getFirst(), i, 0));
        }

        // define a counter which will keep track of the median index (when to stop).
        Integer counter = 0;

        // while the counter has not reached the median element. This will run for O(nm/2) time.
        while (counter != medianIndex) {
            // get the smallest element in O(log(n)) time & increment the counter value.
            HeapElement<Integer> element = minHeap.pop();
            counter += 1;

            // if the next element to the popped element is available, then push it into the min heap in
            // O(log(n)) time.
            if (0 <= element.getColIndex() + 1 && element.getColIndex() + 1 < m) {
                minHeap.insert(new HeapElement<>(matrix.get(element.getRowIndex()).get(element.getColIndex() + 1) , element.getRowIndex(), element.getColIndex() + 1));
            }
        }

        // the top of heap will point to the median, return it in O(log(n)) time.
        return minHeap.pop().getValue();
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