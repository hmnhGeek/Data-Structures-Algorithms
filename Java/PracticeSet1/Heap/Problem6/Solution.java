package PracticeSet1.Heap.Problem6;

import java.util.ArrayList;
import java.util.Arrays;
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
                mergeKSortedArrays(
                        Arrays.asList(
                                Arrays.asList(1, 3, 5, 7),
                                Arrays.asList(2, 4, 6, 8),
                                Arrays.asList(0, 9, 10, 11)
                        )
                )
        );
    }

    public static <T extends Comparable<T>> List<T> mergeKSortedArrays(List<List<T>> mtx) {
        MinHeap<HeapElement<T>> minHeap = new MinHeap<>();
        int n = mtx.size(), m = mtx.getFirst().size();
        for (int i = 0; i < n; i += 1) {
            minHeap.insert(new HeapElement<>(mtx.get(i).getFirst(), i, 0));
        }
        List<T> result = new ArrayList<>();
        while (!minHeap.isEmpty()) {
            HeapElement<T> heapElement = minHeap.pop();
            result.add(heapElement.data);
            int i = heapElement.i, j = heapElement.j;
            if (0 <= j + 1 && j + 1 < m) {
                minHeap.insert(new HeapElement<>(mtx.get(i).get(j + 1), i, j + 1));
            }
        }
        return result;
    }
}
