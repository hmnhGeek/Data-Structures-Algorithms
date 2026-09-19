package StacksAndQueues.Problem21;

public class Queue<T> {
    private Deque<T> deque;

    public Queue() {
        this.deque = new Deque<>();
    }

    public Integer size() {
        return this.deque.size();
    }

    public boolean isEmpty() {
        return this.deque.isEmpty();
    }

    public void enqueue(T x) {
        this.deque.pushBack(x);
    }

    public T dequeue() {
        return this.deque.popFront();
    }
}
