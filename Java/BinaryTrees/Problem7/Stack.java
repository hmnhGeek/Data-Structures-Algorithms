package BinaryTrees.Problem7;

class StackNode<T> {
    private T data;
    private StackNode<T> next;

    public StackNode(T data) {
        this.data = data;
        this.next = null;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public StackNode<T> getNext() {
        return next;
    }

    public void setNext(StackNode<T> next) {
        this.next = next;
    }
}

public class Stack<T> {
    private StackNode<T> head;
    private StackNode<T> tail;
    private Integer length;

    public Stack() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void push(T x) {
        StackNode<T> node = new StackNode<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        } else {
            node.setNext(this.head);
            this.head = node;
        }
        this.length += 1;
    }

    public T pop() {
        if (isEmpty()) return null;
        T item = this.head.getData();
        this.head = this.head.getNext();
        this.length -= 1;
        return item;
    }
}
