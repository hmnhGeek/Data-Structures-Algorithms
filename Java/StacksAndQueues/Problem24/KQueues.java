package StacksAndQueues.Problem24;

import java.util.*;

enum Pointer {
    FRONT, BACK;
}

public class KQueues<T> {
    public Integer numQueues;
    public Integer arraySize;
    private Integer queueSize;
    private Map<Integer, Map<Pointer, Integer>> pointers;
    private List<T> arr;

    public List<T> getArr() {
        return arr;
    }

    public KQueues(Integer numQueues, Integer arraySize) {
        this.numQueues = numQueues;
        this.arraySize = arraySize;
        this.queueSize = arraySize / numQueues;
        arrayInit();
        initPointers();
    }

    private void initPointers() {
        this.pointers = new HashMap<>();
        for (int i = 0; i < this.numQueues; i += 1) {
            this.pointers.put(i, new HashMap<>());
            this.pointers.get(i).put(Pointer.FRONT, this.queueSize * i);
            this.pointers.get(i).put(Pointer.BACK, this.queueSize * i);
        }
    }

    private void arrayInit() {
        this.arr = new ArrayList<>();
        for (int i = 0; i < this.arraySize; i += 1) {
            this.arr.add(null);
        }
    }

    private Integer getFront(int qn) {
        return this.pointers.get(qn).get(Pointer.FRONT);
    }

    private Integer getBack(int qn) {
        return this.pointers.get(qn).get(Pointer.BACK);
    }

    public boolean isEmpty(int qn) {
        int f = getFront(qn), b = getBack(qn);
        return Objects.equals(f, b) && this.arr.get(b) == null;
    }

    public boolean isFull(int qn) {
        int f = getFront(qn), b = getBack(qn);
        return Objects.equals(f, b) &&  this.arr.get(b) != null;
    }

    private int getStartIndexOfQueueFromArray(int qn) {
        return qn * this.queueSize;
    }

    private void incrementBack(int qn) {
        int idx = getBack(qn);

        // if b + 1 flows out of the array, circle back it to the start of the qn part.
        if (idx + 1 == this.arr.size()) {
            this.pointers.get(qn).put(Pointer.BACK, this.queueSize * qn);
        }

        // if b + 1 flows to the start index of qn + 1, circle it back to the start of the qn part.
        else if (idx + 1 == getStartIndexOfQueueFromArray(qn + 1)) {
            this.pointers.get(qn).put(Pointer.BACK, this.queueSize * qn);
        }

        // Otherwise, simply increment the back pointer.
        else {
            this.pointers.get(qn).put(Pointer.BACK, this.pointers.get(qn).get(Pointer.BACK) + 1);
        }
    }

    private void incrementFront(int qn) {
        // Same logic as for back pointer.
        int idx = getFront(qn);
        if (idx + 1 == this.arr.size()) {
            this.pointers.get(qn).put(Pointer.FRONT, this.queueSize * qn);
        }
        else if (idx + 1 == getStartIndexOfQueueFromArray(qn + 1)) {
            this.pointers.get(qn).put(Pointer.FRONT, this.queueSize * qn);
        }
        else {
            this.pointers.get(qn).put(Pointer.FRONT, this.pointers.get(qn).get(Pointer.FRONT) + 1);
        }
    }

    public void enqueue(int qn, T x) {
        /*
            Time complexity for enqueue operation is O(1) and space complexity is O(n + k).
            Why n + k? n for array and k for pointers map.
         */

        // checking if queue is full takes O(1) time.
        if (isFull(qn)) {
            System.out.printf("The queue %d is full. Cannot insert element %s.%n", qn, x);
            return;
        }

        // putting element in array takes O(1) time.
        this.arr.set(getBack(qn), x);

        // This operation also takes O(1) time.
        incrementBack(qn);
    }

    public T dequeue(int qn) {
        /*
            Time complexity for enqueue operation is O(1) and space complexity is O(n + k).
            Why n + k? n for array and k for pointers map.
         */

        // checking if queue is empty takes O(1) time.
        if (isEmpty(qn)) return null;

        // This is also a O(1) time operation.
        T item = this.arr.get(getFront(qn));

        // setting an element to null is O(1) time operation.
        this.arr.set(getFront(qn), null);

        // This is also O(1) time operation.
        incrementFront(qn);
        return item;
    }
}
