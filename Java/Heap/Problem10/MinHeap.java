package Heap.Problem10;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MinHeap<T extends Comparable<T>> implements Heap<T> {
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
        if (lci == null && rci == null) return null;
        if (lci == null) return rci;
        if (rci == null) return lci;
        Integer minChildIndex = lci;
        if (this.heap.get(rci).compareTo(this.heap.get(minChildIndex)) < 0) {
            minChildIndex = rci;
        }
        return minChildIndex;
    }

    @Override
    public void heapifyUp(Integer startIndex) {
        if (startIndex == 0) return;
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
