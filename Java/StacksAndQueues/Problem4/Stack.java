package StacksAndQueues.Problem4;


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

    public Node<T> getHead() {
        return head;
    }

    public void setHead(Node<T> head) {
        this.head = head;
    }

    public Node<T> getTail() {
        return tail;
    }

    public void setTail(Node<T> tail) {
        this.tail = tail;
    }

    public Integer getLength() {
        return length;
    }

    public void setLength(Integer length) {
        this.length = length;
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (getLength().equals(0)) {
            setHead(node);
            setTail(node);
        } else {
            node.setNext(getHead());
            setHead(node);
        }
        setLength(getLength() + 1);
    }

    public T pop() {
        if (getLength().equals(0)) return null;
        T item = getHead().getData();
        setHead(getHead().getNext());
        setLength(getLength() - 1);
        return item;
    }
}
