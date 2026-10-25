package StacksAndQueues.Problem23;

public class Queue<T> {
    public Stack<T> stack1, stack2;

    public Queue() {
        this.stack1 = new Stack<>();
        this.stack2 = new Stack<>();
    }

    public Integer size() {
        return this.stack1.length;
    }

    public boolean isEmpty() {
        return this.size().equals(0);
    }

    public void enqueue(T x) {
        while (!stack1.isEmpty()) {
            stack2.push(stack1.pop());
        }
        stack1.push(x);
        while (!stack2.isEmpty()) {
            stack1.push(stack2.pop());
        }
    }

    public T dequeue() {
        return stack1.pop();
    }

    public T front() {
        return stack1.top();
    }
}
