package StacksAndQueues.Problem3;

import java.util.ArrayList;
import java.util.List;

public class TwoStacks<T> {
    private List<T> stacks;
    private Integer i;
    private Integer j;

    public TwoStacks() {
        stacks = new ArrayList<>();
        stacks.add(null);
        stacks.add(null);
        i = 0;
        j = 1;
    }

    public void push1(T x) {
        stacks.set(i, x);
        if (i + 2 < stacks.size()) {
            i += 2;
        } else if (i + 1 < stacks.size()) {
            stacks.add(null);
            i += 2;
        } else {
            stacks.add(null);
            stacks.add(null);
            i += 2;
        }
    }

    public void push2(T x) {
        stacks.set(j, x);
        if (j + 2 < stacks.size()) {
            j += 2;
        } else if (j + 1 < stacks.size()) {
            stacks.add(null);
            j += 2;
        } else {
            stacks.add(null);
            stacks.add(null);
            j += 2;
        }
    }

    public T pop1() {
        if (i == 0) return null;
        T item = stacks.get(i - 2);
        i -= 2;
        stacks.set(i, null);
        return item;
    }

    public T pop2() {
        if (j == 1) return null;
        T item = stacks.get(j - 2);
        j -= 2;
        stacks.set(j, null);
        return item;
    }
}
