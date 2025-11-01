package Heap.Problem12;

import java.util.Collections;
import java.util.List;

public interface Heap<T extends Comparable<T>> {
    List<T> getHeap();
    Integer getChildIndex(Integer lci, Integer rci);
    void heapifyUp(Integer startIndex);
    void heapifyDown(Integer pi);

    default boolean isEmpty() {
        return getHeap().isEmpty();
    }

    default T top() {
        if (isEmpty()) return null;
        return getHeap().getFirst();
    }

    default Integer getLci(Integer pi) {
        Integer lci = 2*pi + 1;
        if (0 <= lci && lci < getHeap().size()) {
            return lci;
        }
        return null;
    }

    default Integer getRci(Integer pi) {
        Integer rci = 2*pi + 2;
        if (0 <= rci && rci < getHeap().size()) {
            return rci;
        }
        return null;
    }

    default Integer getPi(Integer ci) {
        if (ci == 0) return null;
        Integer pi = (ci - 1)/2;
        if (0 <= pi && pi < getHeap().size()) {
            return pi;
        }
        return null;
    }

    default void push(T x) {
        getHeap().add(x);
        heapifyUp(getHeap().size() - 1);
    }

    default T pop() {
        if (isEmpty()) return null;
        T item = getHeap().getFirst();
        Collections.swap(getHeap(), 0, getHeap().size() - 1);
        getHeap().removeLast();
        heapifyDown(0);
        return item;
    }
}
