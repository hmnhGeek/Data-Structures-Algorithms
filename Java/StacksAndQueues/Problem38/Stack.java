package StacksAndQueues.Problem38;

class Node<T> {
    private T data;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }
}


public class Stack<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public Stack() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            node.setNext(this.head);
            this.head = node;
        }
        this.length += 1;
    }

    public T pop() {
        if (isEmpty()) {
            return null;
        }
        T item = this.head.getData();
        this.head = this.head.getNext();
        this.length -= 1;
        return item;
    }

    public T top() {
        if (isEmpty()) return null;
        return this.head.getData();
    }
}
