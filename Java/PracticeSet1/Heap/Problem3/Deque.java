package PracticeSet1.Heap.Problem3;


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

    public T getBack() {
        if (isEmpty()) return null;
        return this.tail.data;
    }

    public T getFront() {
        if (isEmpty()) return null;
        return this.head.data;
    }

    public T popBack() {
        if (isEmpty()) return null;
        T item = this.tail.data;
        this.tail = this.tail.prev;
        this.tail.next = null;
        this.length -= 1;
        return item;
    }
}
