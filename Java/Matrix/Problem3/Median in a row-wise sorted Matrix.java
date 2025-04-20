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
        Integer n = matrix.size(), m = matrix.getFirst().size();
        Integer medianIndex = (n * m)/2;
        MinHeap<HeapElement<Integer>> minHeap = new MinHeap<>();
        for (int i = 0; i < n; i += 1) {
            minHeap.insert(new HeapElement<>(matrix.get(i).getFirst(), i, 0));
        }
        Integer counter = 0;
        while (counter != medianIndex) {
            HeapElement<Integer> element = minHeap.pop();
            counter += 1;
            if (0 <= element.getColIndex() + 1 && element.getColIndex() < m) {
                minHeap.insert(new HeapElement<>(matrix.get(element.getRowIndex()).get(element.getColIndex() + 1) , element.getRowIndex(), element.getColIndex() + 1));
            }
        }
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
    }
}