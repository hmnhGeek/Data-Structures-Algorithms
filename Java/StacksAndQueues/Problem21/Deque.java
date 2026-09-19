package StacksAndQueues.Problem21;


class Node<T> {
    public T data;
    public Node<T> prev, next;

    public Node(T data) {
        this.data = data;
        this.prev = this.next = null;
    }
}


public class Deque<T> {
    public Node<T> head, tail;
    public Integer length;

    public Deque() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public Integer size() {
        return this.length;
    }

    public void pushFront(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            node.next = this.head;
            this.head.prev = node;
            this.head = node;
        }
        this.length += 1;
    }

    public void pushBack(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        }
        this.length += 1;
    }

    public T popFront() {
        if (isEmpty()) return null;
        T item = this.head.data;
        this.head = this.head.next;
        if (this.head != null) {
            this.head.prev = null;
        }
        this.length -= 1;
        return item;
    }

    public T popBack() {
        if (isEmpty()) return null;
        T item = this.tail.data;
        this.tail = this.tail.prev;
        if (this.tail != null) {
            this.tail.next = null;
        }
        this.length -= 1;
        return item;
    }
}
