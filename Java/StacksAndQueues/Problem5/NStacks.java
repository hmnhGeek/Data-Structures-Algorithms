package StacksAndQueues.Problem5;

import java.util.ArrayList;
import java.util.List;

public class NStacks<T> {
    private List<T> stackArray;
    private List<Integer> tops;
    private List<Integer> next;
    private Integer freeIndex;

    public NStacks(Integer n, Integer k) {
        this.stackArray = new ArrayList<>(n);
        for (int i = 0; i < n; i += 1) {
            this.stackArray.add(null);
        }

        this.tops = new ArrayList<>(k);
        for (int i = 0; i < k; i += 1) {
            this.tops.add(-1);
        }

        this.next = new ArrayList<>(n);
        for (int i = 0; i < n - 1; i += 1) {
            this.next.add(i + 1);
        }
        this.next.add(-1);

        this.freeIndex = 0;
    }

    public void push(T x, int stack) {
        int s = stack - 1;
        int index = freeIndex;
        this.stackArray.set(index, x);
        freeIndex = this.next.get(index);
        this.next.set(index, this.tops.get(s));
        this.tops.set(s, index);
        System.out.println(this.stackArray);
    }

    public T pop(int stack) {
        int s = stack - 1;
        if (this.tops.get(s).equals(-1)) return null;
        int index = this.tops.get(s);
        T elem = this.stackArray.get(index);
        this.stackArray.set(index, null);
        this.tops.set(s, this.next.get(index));
        this.next.set(index, freeIndex);
        freeIndex = index;
        System.out.println(this.stackArray);
        return elem;
    }
}
