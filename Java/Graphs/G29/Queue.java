package Graphs.G29;


class Node<T> {
    public T data;
    public Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}


public class Queue<T> {
    public Node<T> head;
    public Node<T> tail;
    public Integer length;

    public Queue() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return length.equals(0);
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            head = tail = node;
        } else {
            tail.next = node;
            tail = node;
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
}
