package Graphs.G8;

public class Queue<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public Queue() {
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
            this.tail.setNext(node);
            this.tail = node;
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
}
