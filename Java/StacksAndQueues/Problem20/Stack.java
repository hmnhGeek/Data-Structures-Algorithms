package StacksAndQueues.Problem20;

public class Stack<T> {
    private Queue<T> q1;
    private Queue<T> q2;

    public Stack() {
        this.q1 = new Queue<>();
        this.q2 = new Queue<>();
    }

    public void push(T x) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        while (!q1.isEmpty()) {
            q2.enqueue(q1.dequeue());
        }
        q1.enqueue(x);
        while (!q2.isEmpty()) {
            q1.enqueue(q2.dequeue());
        }
    }

    public T top() {
        /*
            T : O(1) and S : O(1)
         */
        if (q1.isEmpty()) return null;
        return q1.front();
    }

    public Integer size() {
        /*
            T : O(1) and S : O(1)
         */
        return q1.length;
    }

    public T pop() {
        /*
            T : O(1) and S : O(1)
         */
        if (q1.isEmpty()) return null;
        return q1.dequeue();
    }
}
