package StacksAndQueues.Problem21;

public class Stack<T> {
    private Deque<T> deque;

    public Stack() {
        this.deque = new Deque<>();
    }

    public Integer size() {
        return this.deque.size();
    }

    public boolean isEmpty() {
        return this.deque.isEmpty();
    }

    public void push(T x) {
        this.deque.pushBack(x);
    }

    public T pop() {
        return this.deque.popBack();
    }
}
