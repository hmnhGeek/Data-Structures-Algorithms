package Heap.Problem7;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MaxHeap<T extends Comparable<T>> implements Heap<T> {
    private List<T> heap;

    public MaxHeap() {
        this.heap = new ArrayList<>();
    }

    @Override
    public List<T> getHeap() {
        return heap;
    }

    @Override
    public Integer getChildIndex(Integer lci, Integer rci) {
        if (lci == null && rci == null) return null;
        if (lci == null) return rci;
        if (rci == null) return lci;
        Integer maxChildIndex = lci;
        if (this.heap.get(rci).compareTo(this.heap.get(lci)) > 0) {
            maxChildIndex = rci;
        }
        return maxChildIndex;
    }

    @Override
    public void heapifyUp(Integer startIndex) {
        if (startIndex == 0) return;
        Integer pi = getPi(startIndex);
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer maxChildIndex = getChildIndex(lci, rci);
        if (maxChildIndex != null) {
            if (this.heap.get(pi).compareTo(this.heap.get(maxChildIndex)) < 0) {
                Collections.swap(this.heap, pi, maxChildIndex);
            }
            heapifyUp(pi);
        }
    }

    @Override
    public void heapifyDown(Integer pi) {
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer maxChildIndex = getChildIndex(lci, rci);
        if (maxChildIndex != null) {
            if (this.heap.get(pi).compareTo(this.heap.get(maxChildIndex)) < 0) {
                Collections.swap(this.heap, pi, maxChildIndex);
            }
            heapifyDown(maxChildIndex);
        }
    }
}
