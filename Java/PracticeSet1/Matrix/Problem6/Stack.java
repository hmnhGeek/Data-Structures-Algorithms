package PracticeSet1.Matrix.Problem6;


class Node<T> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class Stack<T> {
    public Node<T> head, tail;
    public Integer length;

    public Stack() {
        head = tail = null;
        length = 0;
    }

    public boolean isEmpty() {
        return length == 0;
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            head = tail = node;
        } else {
            node.next = head;
            head = node;
        }
        length += 1;
    }

    public T pop() {
        if (isEmpty()) return null;
        T item = head.data;
        head = head.next;
        length -= 1;
        return item;
    }

    public T top() {
        if (isEmpty()) return null;
        return head.data;
    }
}
