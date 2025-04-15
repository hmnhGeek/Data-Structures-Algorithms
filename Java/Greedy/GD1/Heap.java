package Greedy.GD1;

import java.util.Collections;
import java.util.List;

interface Heap<T extends Comparable<T>> {
    List<T> getHeap();

    default boolean isEmpty() {
        return getHeap().isEmpty();
    }

    default Integer getLci(Integer pi) {
        int lci = 2*pi + 1;
        return 0 <= lci && lci < getHeap().size() ? lci : null;
    }

    default Integer getRci(Integer pi) {
        int rci = 2*pi + 2;
        return 0 <= rci && rci < getHeap().size() ? rci : null;
    }

    default Integer getPi(Integer ci) {
        int pi = (ci - 1)/2;
        return 0 <= pi && pi < getHeap().size() ? pi : null;
    }

    Integer getChildIndex(Integer lci, Integer rci);

    void heapifyUp(Integer startIndex);

    void heapifyDown(Integer pi);

    default void insert(T x) {
        getHeap().add(x);
        heapifyUp(getHeap().size() - 1);
    }

    default T pop() {
        if (isEmpty()) {
            return null;
        }
        T item = getHeap().getFirst();
        Collections.swap(getHeap(), 0, getHeap().size() - 1);
        getHeap().removeLast();
        heapifyDown(0);
        return item;
    }
}
