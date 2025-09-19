package StacksAndQueues.Problem6;


class Node<T> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class Stack<T> {
    public Node<T> head;
    public Node<T> tail;
    public Integer length;

    public Stack() {
        this.length = 0;
        this.head = this.tail = null;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public Node<T> push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            node.next = this.head;
            this.head = node;
        }
        this.length += 1;
        return node;
    }

    public T pop() {
        if (isEmpty()) return null;
        T item = this.head.data;
        this.head = this.head.next;
        this.length -= 1;
        return item;
    }
}
