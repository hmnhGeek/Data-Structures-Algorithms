package Heap.Problem17;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MaxHeap<T extends Comparable<T>> {
    public List<T> heap;

    public MaxHeap() {
        this.heap = new ArrayList<>();
    }

    public boolean isEmpty() {
        return this.heap.isEmpty();
    }

    public Integer getLci(Integer pi) {
        int lci = 2 * pi + 1;
        if (0 <= lci && lci < this.heap.size()) {
            return lci;
        }
        return null;
    }

    public Integer getRci(Integer pi) {
        int rci = 2 * pi + 2;
        if (0 <= rci && rci < this.heap.size()) {
            return rci;
        }
        return null;
    }

    public Integer getPi(Integer ci) {
        if (ci == 0) return null;
        int pi = (ci - 1)/2;
        if (0 <= pi && pi < this.heap.size()) {
            return pi;
        }
        return null;
    }

    public Integer getMaxChildIndex(Integer lci, Integer rci) {
        if (lci == null && rci == null) return null;
        if (lci == null) return rci;
        if (rci == null) return lci;
        Integer maxChildIndex = lci;
        if (this.heap.get(rci).compareTo(this.heap.get(lci)) > 0) {
            maxChildIndex = rci;
        }
        return maxChildIndex;
    }

    public void maxHeapifyUp(Integer startIndex) {
        if (startIndex == 0) return;
        int pi = getPi(startIndex);
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer maxChildIndex = getMaxChildIndex(lci, rci);
        if (maxChildIndex != null) {
            if (this.heap.get(pi).compareTo(this.heap.get(maxChildIndex)) < 0) {
                Collections.swap(this.heap, pi, maxChildIndex);
            }
            this.maxHeapifyUp(pi);
        }
    }

    public void maxHeapifyDown(Integer pi) {
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer maxChildIndex = getMaxChildIndex(lci, rci);
        if (maxChildIndex != null) {
            if (this.heap.get(pi).compareTo(this.heap.get(maxChildIndex)) < 0) {
                Collections.swap(this.heap, pi, maxChildIndex);
            }
            this.maxHeapifyDown(maxChildIndex);
        }
    }

    public void insert(T x) {
        this.heap.add(x);
        maxHeapifyUp(this.heap.size() - 1);
    }

    public T pop() {
        if (isEmpty()) return null;
        T item = this.heap.getFirst();
        Collections.swap(this.heap, 0, this.heap.size() - 1);
        this.heap.removeLast();
        this.maxHeapifyDown(0);
        return item;
    }
}
