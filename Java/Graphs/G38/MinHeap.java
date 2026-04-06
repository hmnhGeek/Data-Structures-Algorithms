package Graphs.G38;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MinHeap<T extends Comparable<T>> {
    public List<T> heap;

    public MinHeap() {
        this.heap = new ArrayList<>();
    }

    public List<T> getHeap() {
        return this.heap;
    }

    public boolean isEmpty() {
        return getHeap().isEmpty();
    }

    public Integer getLci(Integer pi) {
        Integer lci = 2*pi + 1;
        if (0 <= lci && lci < getHeap().size()) return lci;
        return null;
    }

    public Integer getRci(Integer pi) {
        Integer rci = 2*pi + 2;
        if (0 <= rci && rci < getHeap().size()) return rci;
        return null;
    }

    public Integer getPi(Integer ci) {
        if (ci == 0) return null;
        Integer pi = (ci - 1)/2;
        if (0 <= pi && pi < getHeap().size()) return pi;
        return null;
    }

    public Integer getMinChildIndex(Integer lci, Integer rci) {
        if (lci == null && rci == null) return null;
        if (lci == null) return rci;
        if (rci == null) return lci;
        Integer minChildIndex = lci;
        if (getHeap().get(rci).compareTo(getHeap().get(minChildIndex)) < 0) {
            minChildIndex = rci;
        }
        return minChildIndex;
    }

    public void minHeapifyUp(Integer startIndex) {
        if (startIndex == 0) return;
        Integer pi = getPi(startIndex);
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer minChildIndex = getMinChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (getHeap().get(pi).compareTo(getHeap().get(minChildIndex)) > 0) {
                Collections.swap(getHeap(), pi, minChildIndex);
            }
            minHeapifyUp(pi);
        }
    }

    public void minHeapifyDown(Integer pi) {
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer minChildIndex = getMinChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (getHeap().get(pi).compareTo(getHeap().get(minChildIndex)) > 0) {
                Collections.swap(getHeap(), pi, minChildIndex);
            }
            minHeapifyDown(minChildIndex);
        }
    }

    public void insert(T x) {
        getHeap().add(x);
        minHeapifyUp(getHeap().size() - 1);
    }

    public T pop() {
        if (isEmpty()) return null;
        T item = getHeap().getFirst();
        Collections.swap(getHeap(), 0, getHeap().size() - 1);
        getHeap().removeLast();
        minHeapifyDown(0);
        return item;
    }
}
