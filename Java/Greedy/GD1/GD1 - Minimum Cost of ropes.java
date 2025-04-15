package Greedy.GD1;

import java.util.ArrayList;
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
        if (getHeap().get(rci).compareTo(getHeap().get(minChildIndex)) < 0) {
            minChildIndex = rci;
        }
        return minChildIndex;
    }

    @Override
    public void heapifyUp(Integer startIndex) {
        if (startIndex.equals(0)) return;
        int pi = getPi(startIndex);
        int lci = getLci(pi), rci = getRci(pi);
        Integer minChildIndex = getChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (getHeap().get(pi).compareTo(getHeap().get(minChildIndex)) > 0) {
                Collections.swap(getHeap(), pi, minChildIndex);
            }
            heapifyUp(pi);
        }
    }

    @Override
    public void heapifyDown(Integer pi) {
        int lci = getLci(pi), rci = getRci(pi);
        Integer minChildIndex = getChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (getHeap().get(pi).compareTo(getHeap().get(minChildIndex)) > 0) {
                Collections.swap(getHeap(), pi, minChildIndex);
            }
            heapifyDown(minChildIndex);
        }
    }
}

class SolutionGD1 {
    public static Integer getMinCostToConnectRopes(List<Integer> ropes) {
        MinHeap<Integer> minHeap = new MinHeap<>();
        ropes.forEach(minHeap::insert);
    }
}