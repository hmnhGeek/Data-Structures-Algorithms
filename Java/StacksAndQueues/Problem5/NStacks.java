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
        /*
            Time complexity is O(1) and space complexity is O(2n + k).
         */

        // check if we have free space to push in a new element. If freeIndex becomes -1, then it means that the
        // original array is full.
        if (freeIndex.equals(-1)) return;

        // get the stack index in 0-based format.
        int s = stack - 1;

        // store index of the free slot.
        int index = freeIndex;

        // put the element x into the free slot.
        this.stackArray.set(index, x);

        // update free to point to next slot in free list
        freeIndex = this.next.get(index);

        // update next to point to the previous element index of the stack s.
        this.next.set(index, this.tops.get(s));

        // update top to point at the current filled index.
        this.tops.set(s, index);

        // print the stack only for informational purposes.
        System.out.println(this.stackArray);
    }

    public T pop(int stack) {
        /*
            Time complexity is O(1) and space complexity is O(2n + k).
         */

        // get the stack index.
        int s = stack - 1;

        // if the stack's top is -1, its empty.
        if (this.tops.get(s).equals(-1)) return null;

        // get index of top item in stack s.
        int index = this.tops.get(s);

        // get the element at index and set the value as null in the original array.
        T elem = this.stackArray.get(index);
        this.stackArray.set(index, null);

        // since next points to previous element, update top with it.
        this.tops.set(s, this.next.get(index));

        // set next to the free available index.
        this.next.set(index, freeIndex);

        // update free index to the current index because it got free just now.
        freeIndex = index;

        // print the stack
        System.out.println(this.stackArray);

        // return the element.
        return elem;
    }
}
