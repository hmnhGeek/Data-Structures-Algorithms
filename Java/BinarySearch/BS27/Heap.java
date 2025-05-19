package BinarySearch.BS27;

import java.util.List;

public interface Heap<T extends Comparable<T>> {
    List<T> getHeap();
    Integer getChildIndex(Integer lci, Integer rci);
    void heapifyUp(Integer startIndex);
    void heapifyDown(Integer pi);

    default boolean isEmpty() {
        return getHeap().isEmpty();
    }

    default Integer getLci(Integer pi) {
        Integer lci = 2*pi + 1;
        return 0 <= lci && lci < getHeap().size() ? lci : null;
    }

    default Integer getRci(Integer pi) {
        Integer rci = 2*pi + 2;
        return 0 <= rci && rci < getHeap().size() ? rci : null;
    }

    default Integer getPi(Integer ci) {
        if (ci.equals(0)) return null;
        Integer pi = (ci - 1)/2;
        return 0 <= pi && pi < getHeap().size() ? pi : null;
    }
}
