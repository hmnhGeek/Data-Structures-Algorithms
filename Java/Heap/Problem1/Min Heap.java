// Problem link - https://www.geeksforgeeks.org/building-heap-from-array/

package Heap.Problem1;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class MinHeap<T extends Comparable<T>> {
    private List<T> heap;

    public MinHeap() {
        this.heap = new ArrayList<>();
    }

    public boolean isEmpty() {
        return this.heap.isEmpty();
    }

    public Integer getLci(Integer pi) {
        Integer lci = 2*pi + 1;
        return 0 <= lci && lci < this.heap.size() ? lci : null;
    }

    public Integer getRci(Integer pi) {
        Integer rci = 2*pi + 2;
        return 0 <= rci && rci < this.heap.size() ? rci : null;
    }

    public Integer getPi(Integer ci) {
        if (ci == 0) {
            return null;
        }
        Integer pi = (ci - 1)/2;
        return 0 <= pi && pi < this.heap.size() ? pi : null;
    }

    public Integer getMinChildIndex(Integer lci, Integer rci) {
        if (lci == null && rci == null) {
            return null;
        }
        if (lci == null) {
            return rci;
        }
        if (rci == null) {
            return rci;
        }
        Integer minChildIndex = lci;
        if (this.heap.get(rci).compareTo(this.heap.get(lci)) < 0) {
            minChildIndex = rci;
        }
        return minChildIndex;
    }

    public void minHeapifyUp(Integer startIndex) {
        if (startIndex.equals(0)) {
            return;
        }
        Integer pi = getPi(startIndex);
        Integer lci = getLci(pi);
        Integer rci = getRci(pi);
        Integer minChildIndex = getMinChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (this.heap.get(pi).compareTo(this.heap.get(minChildIndex)) > 0) {
                Collections.swap(this.heap, pi, minChildIndex);
            }
            minHeapifyUp(pi);
        }
    }

    public void minHeapifyDown(Integer pi) {
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer minChildIndex = getMinChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (this.heap.get(pi).compareTo(this.heap.get(minChildIndex)) > 0) {
                Collections.swap(this.heap, pi, minChildIndex);
            }
            minHeapifyDown(minChildIndex);
        }
    }

    public void insert(T x) {
        this.heap.add(x);
        minHeapifyUp(this.heap.size() - 1);
    }

    public T pop() {
        if (isEmpty()) {
            return null;
        }
        T item = this.heap.getFirst();
        Collections.swap(this.heap, 0, this.heap.size() - 1);
        this.heap.removeLast();
        minHeapifyDown(0);
        return item;
    }
}


class Solution {
    public static void main(String[] args) {
        useMinHeap(2,1,6,8,4,9,3,2,8,9);
        useMinHeap(4, 10, 3, 5, 1);
        useMinHeap(1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17);
    }

    @SafeVarargs
    public static <T extends Comparable<T>> void useMinHeap(T... args) {
        /**
         * Time complexity is O(n * log(n)) and space complexity is O(n).
         */
        MinHeap<T> minHeap = new MinHeap<>();
        List<T> arr1 = Arrays.asList(args);
        arr1.forEach(minHeap::insert);
        while (!minHeap.isEmpty()) {
            System.out.printf("%s ", minHeap.pop());
        }
        System.out.println();
    }

}