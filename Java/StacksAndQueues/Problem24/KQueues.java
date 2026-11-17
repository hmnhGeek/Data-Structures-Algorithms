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

    private int getStartIndexOfQueueFromArray(int qn) {
        return qn * this.queueSize;
    }

    public boolean isFull(int qn) {
        int f = getFront(qn);
        int b = getBack(qn);
        return Objects.equals(f, b) && this.arr.get(b) != null;
    }

    private void incrementBack(int qn) {
        int idx = getBack(qn);
        if (idx + 1 == this.arr.size()) {
            this.pointers.get(qn).put(Pointer.BACK, this.queueSize * qn);
        }
        else if (idx + 1 == getStartIndexOfQueueFromArray(qn + 1)) {
            this.pointers.get(qn).put(Pointer.BACK, this.queueSize * qn);
        }
        this.pointers.get(qn).put(Pointer.BACK, this.pointers.get(qn).get(Pointer.BACK) + 1);
    }

    private void incrementFront(int qn) {
        int idx = getFront(qn);
        if (idx + 1 == this.arr.size()) {
            this.pointers.get(qn).put(Pointer.FRONT, this.queueSize * qn);
        }
        else if (idx + 1 == getStartIndexOfQueueFromArray(qn + 1)) {
            this.pointers.get(qn).put(Pointer.FRONT, this.queueSize * qn);
        }
        this.pointers.get(qn).put(Pointer.FRONT, this.pointers.get(qn).get(Pointer.FRONT) + 1);
    }

    public void enqueue(int qn, T x) {
        if (isFull(qn)) {
            System.out.printf("The {%d} queue is full. Cannot insert element.%n", qn);
            return;
        }
        this.arr.set(getBack(qn), x);
        incrementBack(qn);
    }

    public T dequeue(int qn) {
        if (isEmpty(qn)) return null;
        T item = this.arr.get(getFront(qn));
        this.arr.set(getFront(qn), null);
        incrementFront(qn);
        return item;
    }
}
