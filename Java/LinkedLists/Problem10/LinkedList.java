package LinkedLists.Problem10;


class Node<T> {
    private T data;
    private Node<T> next;

    public Node(T data) {
        this.next = null;
        this.data = data;
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


public class LinkedList<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public LinkedList() {
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
        if (isEmpty()) return null;
        T item = this.head.getData();
        this.head = this.head.getNext();
        this.length -= 1;
        return item;
    }

    @Override
    public String toString() {
        if (isEmpty()) return "[]";
        if (this.length.equals(1)) return String.format("[%s]", this.head.getData());
        StringBuilder result = new StringBuilder(String.format("[%s, ", this.head.getData()));
        Node<T> curr = this.head.getNext();
        while (curr != this.tail) {
            result.append(String.format("%s, ", curr.getData()));
            curr = curr.getNext();
        }
        result.append(String.format("%s]", this.tail.getData()));
        return result.toString();
    }

    public void build(T...args) {
        for (T arg : args) {
            push(arg);
        }
    }
}
