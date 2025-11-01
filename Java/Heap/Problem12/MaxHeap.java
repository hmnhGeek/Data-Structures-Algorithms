package Heap.Problem12;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MaxHeap<T extends Comparable<T>> implements Heap<T> {
    public List<T> heap;

    public MaxHeap() {
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
        if (lci == null) return rci;
        if (rci == null) return lci;
        Integer maxChildIndex = lci;
        if (heap.get(rci).compareTo(heap.get(maxChildIndex)) > 0) {
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
            if (heap.get(pi).compareTo(heap.get(maxChildIndex)) < 0) {
                Collections.swap(heap, pi, maxChildIndex);
            }
            heapifyUp(pi);
        }
    }

    @Override
    public void heapifyDown(Integer pi) {
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer maxChildIndex = getChildIndex(lci, rci);
        if (maxChildIndex != null) {
            if (heap.get(pi).compareTo(heap.get(maxChildIndex)) < 0) {
                Collections.swap(heap, pi, maxChildIndex);
            }
            heapifyDown(maxChildIndex);
        }
    }
}
